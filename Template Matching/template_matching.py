# Import libs
import cv2
import numpy as np


def read_images(image1, template):
    
    # Make sure that the images are of the same size
    image_1 = cv2.imread(image1)
    tempate_img = cv2.imread(template, cv2.CV_8U)
    return image_1, tempate_img


def template_matching():
    image_pikachus, template_img = read_images('mario.jpg', 'mario_template.png')
    
    img_gray = cv2.cvtColor(image_pikachus, cv2.COLOR_BGR2GRAY)

    w, h = template_img.shape[::-1]

    #img_gray.astype(np.float32)
    #img_gray.astype(np.uint8)
    
    result = cv2.matchTemplate(img_gray, template_img, cv2.TM_CCOEFF_NORMED)
    threshold = 0.5
    loc = np.where( result >= threshold)
    
    for pt in zip(*loc[::-1]):
        cv2.rectangle(image_pikachus, pt, (pt[0] + w, pt[1] + h), (255,255,255), 2)

    cv2.imshow('Detected',image_pikachus)
    
    
if __name__ == '__main__':
    template_matching()