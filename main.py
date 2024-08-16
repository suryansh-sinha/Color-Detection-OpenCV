import cv2
from util import get_limits
from PIL import Image


# blue = [255, 0, 0]
yellow = [0, 255, 255]
cap = cv2.VideoCapture(0)
opened = cap.isOpened()

if cap.isOpened():
    while True:
        ret, frame = cap.read()
        if ret:
            hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            
            # We get a mask of all the pixels containing the yellow color
            # We need to get the color interval for Hue channel.
            lowerLimit, upperLimit = get_limits(color=yellow) 
            mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)
            
            # Converting image from numpy array to pillow image
            mask_ = Image.fromarray(mask)
            
            # Getting the bounding box of the mask using pillow.
            bbox = mask_.getbbox()
            # print(bbox)
            
            if bbox is not None:
                x1, y1, x2, y2 = bbox
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
            
            cv2.imshow('frame', frame)
            if cv2.waitKey(10) & 0xFF==ord('q'):
                break
        else:
            print('Stream ended')
            break
    
cap.release()
cv2.destroyAllWindows()