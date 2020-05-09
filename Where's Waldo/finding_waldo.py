# Import necessary libraries
import numpy as np
import cv2


def read_images(image1, template):
    
    # Make sure that the images are of the same size
    image_1 = cv2.imread(image1)
    tempate_img = cv2.imread(template, cv2.CV_8U)
    return image_1, tempate_img


def find_waldo():
    waldo, template_img = read_images('color_waldo_template.jpg', 'wheres_waldo.jpg')
    
    img_gray = cv2.cvtColor(waldo, cv2.COLOR_BGR2GRAY)

    w, h = template_img.shape[::-1]

    #img_gray.astype(np.float32)
    #img_gray.astype(np.uint8)
    
    result = cv2.matchTemplate(img_gray, template_img, cv2.TM_CCOEFF_NORMED)
    threshold = 0.5
    loc = np.where( result >= threshold)
    
    for pt in zip(*loc[::-1]):
        cv2.rectangle(waldo, pt, (pt[0] + w, pt[1] + h), (255,255,255), 2)

    cv2.imshow('Detected',waldo)
    
    
if __name__ == '__main__':
    find_waldo()