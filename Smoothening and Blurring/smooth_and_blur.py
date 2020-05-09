# Import libs
import numpy as np
import cv2
import matplotlib.pyplot as plt


def read_images(image1):
    
    # Make sure that the images are of the same size
    image_1 = cv2.imread(image1)
    return image_1


def blur_image():
    img = read_images('pikachu.png')
    
    # Increase the value if more blurring is needed
    kernel = np.ones((5,5),np.float32)/25
    dst = cv2.filter2D(img,-1,kernel)
    
    # FILTERING TECHNIQUES
    # blur = cv.GaussianBlur(img,(5,5),0)
    # median = cv.medianBlur(img,5)
    # blur = cv.bilateralFilter(img,9,75,75)

    # Plotting functions
    plt.subplot(121),plt.imshow(img),plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
    plt.xticks([]), plt.yticks([])
    plt.show()
    
    



if __name__ == '__main__':
    blur_image()