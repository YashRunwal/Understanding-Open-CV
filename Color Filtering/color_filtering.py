# Import necessary libraries
# Note:
#   Change the lower and upper colors to adjust the filter according to your need

import numpy as np
import cv2

def color_filtering():
    cap = cv2.VideoCapture(0)
    
    while True:
        _ , frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # Filter
        lower_red = np.array([0, 0, 0])
        upper_red = np.array([255, 255, 255])
        
        # Creating a mask
        mask = cv2.inRange(hsv, lower_red, upper_red)
        result = cv2.bitwise_and(frame, frame, mask=mask)
        
        cv2.imshow('Frame', frame)
        cv2.imshow('Frame', mask)
        cv2.imshow('Frame', result)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        cv2.destroyAllWindows()
        cap.release()


if __name__ == '__main__':
    color_filtering()