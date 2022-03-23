import os
from PIL import Image

def main():
    input = '/Users/bytedance/Documents/tmp/v02c4e0a0000bv2su168lgvj7itpl8mg_h264_360p_3887_crop.jpg'
    output = '/Users/bytedance/Documents/tmp'
    img = Image.open(input)
    width, high = img.size
    crop_width, crop_high = width // 3, high //3
    for raw in range(3):
        for col in range(3):
            box  = (crop_width * col, crop_high * raw, crop_width * (col+1), crop_high*(raw + 1))
            region = img.crop(box)
            region.save(os.path.join(output,'3887_{}_{}.jpg'.format(raw, col)))
    print('Done')


if __name__ == "__main__":
    main()
        
