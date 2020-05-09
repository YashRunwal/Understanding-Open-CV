# Import libs
import cv2


def read_images(image1):
    
    # Make sure that the images are of the same size
    image_1 = cv2.imread(image1)
    return image_1


def apply_gradient(show_laplacian, show_sobel):
    img = read_images('pikachu.png')
    cv2.imshow('Pikachu', img)
    
    laplacian = cv2.Laplacian(img, cv2.CV_64F)
    
    if show_laplacian == 1:
        cv2.imshow('laplacian', laplacian)
    
    sobel_x = cv2.Sobel(img, cv2.CV_64F,1,0,ksize=5)
    sobel_y = cv2.Sobel(img, cv2.CV_64F,0,1,ksize=5)
    
    if show_sobel == 1:
        cv2.imshow('sobel_x', sobel_x)
        cv2.imshow('sobel_y', sobel_y)
        
        
def edge_detect(show_edge, save_image):
    img = read_images('pikachu.png')
    edges = cv2.Canny(img, 100, 200)
    
    if show_edge == 1:
        cv2.imshow('Edges', edges)
        
    if save_image == 1:
        cv2.imwrite('Edge_Pikachu.jpg', edges)
    
    
if __name__ == '__main__':
    edge_detect(show_edge=1, save_image=1)
