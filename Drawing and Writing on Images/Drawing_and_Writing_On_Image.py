# Plotting shapes and writing to the image with user handling system
# This can be converted to the class but it is not necessary

# Import Libraries
import numpy as np
import cv2

# For shapes
start_pt = (0,0)
end_pt = (400,400)
color = (255,0,0)
line_width = 2
center_of_circle = (200,200)
radius = 50

# For writing
font = cv2.FONT_HERSHEY_COMPLEX
start_pt_text = (100, 100)
size_of_text = 1


def read_image():        
    image = cv2.imread('iqAvM8.jpg', cv2.IMREAD_COLOR)
    image = cv2.resize(image, (960, 540))
    return image


def line():
    
    image = read_image()
    # Line
    cv2.line(image, start_pt, end_pt, color, line_width)
    cv2.imshow('Line with the Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    
def rectangle():
    
    image = read_image()
    # rectangle
    cv2.rectangle(image, start_pt, end_pt, color, line_width)
    cv2.imshow('Line with the Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def circle():
    
    image = read_image()
    # circle
    cv2.circle(image, center_of_circle, radius, color, line_width)
    cv2.imshow('Line with the Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    
def polygons():
    
    image = read_image()
    # polygon
    pts = np.array([ [35, 45], [70, 45], [100, 200], [56, 89], [90, 67] ], np.int32)
    cv2.polylines(image, [pts], True, color, line_width)
    cv2.imshow('Line with the Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    
def write_to_image():
    image = read_image()
    
    # write
    cv2.putText(image, 'It works', start_pt_text, font, size_of_text, color)
    cv2.imshow('Line with the Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    
def input_handling():
    
    print('This prompt is for user to select the function they want to display')
    print('a for read_image()')
    print('b for line()')
    print('c for rectangle()')
    print('d for polygons()')
    print('e for write_to_image()')

    func = input('Any letter between a and e: ')
    
    if func == 'a':
        read_image()
        
    elif func == 'b':
        line()
            
    elif func == 'c':
        rectangle()
            
    elif func == 'd':
        polygons()
        
    elif func == 'e':
        write_to_image()
        
    else:
        print('Please select the letter between a and e')
      
        
        
if __name__ == '__main__':
    input_handling()