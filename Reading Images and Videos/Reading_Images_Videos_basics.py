# This code is just implementation of basics of reading images and Videos
# Made this object oriented just to spearate out the code and for good readability

# Import necessary libraries
import matplotlib.pyplot as plt
import cv2


class Basics_of_OpenCV:
    
    def __init__(self):
        pass
    
    
    def read_image_with_cv(self, image, do_plot = 1, is_gray = 0):
    
        # Read and Resize the Image
        while True:
            
            try:
                if is_gray == 1:
                    show_image = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
                    show_image = cv2.resize(show_image, (960, 540))
                else:
                    show_image = cv2.imread(image, cv2.IMREAD_COLOR)
                    show_image = cv2.resize(show_image, (960, 540))
                       
                # Check the condition for plotting
                if do_plot == 1:
                    cv2.imshow('Image', show_image)      
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
                else:
                    return print('Image Created but not shown')
            
            except ValueError:
                print('Oops, do_plot and is_gray values should be either 1 or 0')
                
                
        
    
    def read_image_with_pyplot(self, image, do_plot = 1):
        
        # Read the Image
        show_image_with_plt = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
        
        # Check the condition for plotting
        if do_plot == 1:
            plt.imshow(show_image_with_plt, cmap='gray')
            plt.show()
        else:
            return print('Image Created but not shown')
        

    
    def capture_video(self, show_gray=1, write_video = 0):
        
        # Video breaks down frames and frames are just like images
        # Use Webcam to capture images
        cap = cv2.VideoCapture(0)
                
        while True:
            ret, frame = cap.read()
            cv2.imshow('Frame', frame)
            
            if show_gray == 1:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                cv2.imshow('Gray Frame', gray)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
        # Write the Video to a folder
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        
        if write_video == 1:
            out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
            out.release()
        
        
        cap.release()
        cv2.destroyAllWindows()


 
if __name__ == '__main__':
    object_1 = Basics_of_OpenCV()
    object_1.read_image_with_cv('iqAvM8.jpg', do_plot=1, is_gray=1)
    # object_1.read_image_with_pyplot('iqAvM8.jpg', 0)
    # object_1.capture_video(show_gray=0, write_video=0)