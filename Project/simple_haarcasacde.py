# Import libraries
import numpy as np
import cv2
import  matplotlib.pyplot as plt

class HaarCascade:
        
    def __init__(self, face, eye):
        
        # Read the xml files
        self.face = cv2.CascadeClassifier(face)
        self.eye = cv2.CascadeClassifier(eye)
    
    
    def capture_video(self):
        
        # Capture Video
        cap = cv2.VideoCapture(0)
        red_color = (0,0,255)
        green_color = (0, 255, 0)
        
        while True:
            _ , img = cap.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = self.face.detectMultiScale(gray, 1.3, 5)
            
            for (x, y, width, height) in faces:
                cv2.rectangle(img, (x,y), (x+width, y+height), red_color, 2)
                region_gray = gray[y:y+height, x:x+width]
                region_color = img[y:y+height, x:x+width]
                
                eyes = self.eye.detectMultiScale(region_gray)
                for (eye_x, eye_y, eye_width, eye_height) in eyes:
                    cv2.rectangle(region_color, (eye_x,eye_y), (eye_x+eye_width, eye_y+eye_height), green_color, 2)
            
#            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            cv2.imshow('Image', img)
            k = cv2.waitKey(30) & 0xff
            if k == 27:
                break
            elif k == ord('s'): # wait for 's' key to save and exit
                cv2.imwrite('img.png',img)
            
        cap.release()
        cap.destroyAllWindows()
            
            
            
if __name__ == '__main__':
    face = 'haarcascade_frontalface_default.xml'
    eye = 'haarcascade_eye.xml'
    c1 = HaarCascade(face, eye)
    c1.capture_video()
