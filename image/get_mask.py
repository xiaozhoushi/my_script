import cv2
import os


def threshold(img, path):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    closed = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel, iterations=3)
    cv2.imwrite(os.path.join(path,'undistorted_mask.bmp'), closed)

if __name__ == '__main__':
    input_path = '/Users/Documents/data/colonoscopy_images/04'
    projects = [project for project in os.listdir(input_path) if '.' != project[0]]
    for project in projects:
        save_path = os.path.join(input_path, project)
        image_list = [img for img in os.listdir(os.path.join(save_path, 'images')) if '.jpg' in img]

        img_one_path = os.path.join(save_path, 'images', image_list[0])
        img = cv2.imread(img_one_path)
        threshold(img, save_path)
