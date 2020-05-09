# Import Libraries
import numpy as np
import cv2


class Corner:
    
    def __init__(self, input_img):
        self.input_img = input_img

    
    # Read Images
    def read_image(self):        
        
        # Read and convert to gray scale
        self.image = cv2.imread(self.input_img)
        self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        
        # Float 32 needed because it is the datatype required in corner detection algo.
        self.gray = np.float32(self.gray)
        return self.gray
    
    
    # Detect Corners
    def corner_detection(self):

        how_many_corners_max_to_find = 1000
        img_quality = 0.01
        min_dist = 10
        corners = cv2.goodFeaturesToTrack(self.gray, how_many_corners_max_to_find, 
                                          img_quality, min_dist)
        corners = np.int0(corners)
        
        # Loop through corners
        for corner in corners:
            x,y = corner.ravel()
            cv2.circle(self.image, (x,y), 2, 255, -1)
            
        cv2.imshow('Corners', self.image)
        cv2.imwrite('detected1000_corner.jpg', self.image)
        


if __name__ == '__main__':
    c1 = Corner('duomo.jpg')
    c1.read_image()
    c1.corner_detection()