import os
from PIL import Image, ImageFilter

def main():
    input = '/Users/Documents/data/public_data/ETIS/images/16.png'
    output = '/Users/Documents/'
    img = Image.open(input)
    img_blur = img.filter(ImageFilter.GaussianBlur(radius=9))
    img_blur.save(os.path.join(output,'blur.png'))
    print('Done')


if __name__ == "__main__":
    main()
        
