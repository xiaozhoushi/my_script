import os
import glob

def main():
    input = '/Users/bytedance/Documents/data/tmp/CVC-PolypHD'
    path_list = glob.glob(input + '/*_ccba.png')
    for path in path_list:
        name = os.path.basename(path)
        if 'ccba' in name:
            print(name)
            os.remove(path)

    print('Done')


if __name__ == "__main__":
    main()
        
