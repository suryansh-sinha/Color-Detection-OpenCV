import cv2
import numpy as np

def get_limits(color):
    c = np.uint8([[color]]) # insert the bgr values which you want to convert to hsv
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)
    # print("Yellow in HSV: ", hsvC)
    
    lowerLimit = hsvC[0][0][0] - 10, 100, 100
    upperLimit = hsvC[0][0][0] - 10, 255, 255
    
    # print("Lower Limit -> ", lowerLimit)
    # print("Upper Limit -> ", upperLimit)
    
    lowerLimit = np.array(lowerLimit, dtype=np.uint8)
    upperLimit = np.array(upperLimit, dtype=np.uint8)
    # print("\n\nNumpy Array Lower Limit --> ", lowerLimit)
    # print("Numpy Array Upper Limit --> ", upperLimit)
    return lowerLimit, upperLimit

# color = [0, 255, 255]
# print(get_limits(color))