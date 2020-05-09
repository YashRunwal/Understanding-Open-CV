# This code is useful to understand basic opeartions that can be performed with images in opencv

# Import necessary Libraries
import cv2


def read_images(image1s, image2s):
    
    # Make sure that the images are of the same size
    image_1 = cv2.imread(image2s)
    image_2 = cv2.imread(image1s)
    return image_1, image_2



def add_images():
    image_1, image_2 = read_images('3D-Matplotlib.png', 'matplotlib_image1.jpg')

    add = image_1 + image_2 # we can also add using cv.add but it is not useful
    cv2.imshow('Added Images', add)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    
    
def add_wighted_images():
    image_1, image_2 = read_images('3D-Matplotlib.png', 'matplotlib_image1.jpg')

    add = cv2.addWeighted(image_1, 0.6, image_2, 0.4, 0)
    cv2.imshow('Added Images', add)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def super_impose(show_mask):
    
    # Using logical Operations 
    
    image1, image2 = read_images('matplotlib_image1.jpg', 'pikachu.png')        
    
    # Rows cols and channels
    rows, cols, channels = image1.shape
    
    # Define ROI
    region_of_int = image2[0:rows, 0:cols]
    
    # convert to gray
    imageToGray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    
    # Mask
    _ , mask = cv2.threshold(imageToGray, 150, 255, cv2.THRESH_BINARY_INV)
    
    if show_mask == 1:
        cv2.imshow('Mask', mask)
        
    # Logical operations
    mask_inverse = cv2.bitwise_not(mask)
    
    image2_background = cv2.bitwise_and(region_of_int, region_of_int, mask=mask_inverse)
    image1_foreground = cv2.bitwise_and(image1, image1, mask=mask)
    
    # Add Images
    adding = image2_background + image1_foreground
    
    # ROI again
    image2[0:rows, 0:cols] = adding
    
    # Show the image
    cv2.imshow('Superimposed image', adding)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    super_impose(show_mask = 0)


