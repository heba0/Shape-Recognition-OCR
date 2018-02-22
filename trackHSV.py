import cv2
import numpy as np

def callback(x):
    pass

cap = cv2.VideoCapture(0)
cv2.namedWindow('image')
cv2.namedWindow('image2')
##yellow
##ilowH = 4
##ihighH = 73
##
##ilowS = 8
##ihighS = 185
##ilowV = 194
##ihighV = 255


##yellow2
##ilowH = 5
##ihighH = 68
##
##ilowS = 23
##ihighS = 255
##ilowV = 144
##ihighV = 169




ilowH = 0
ihighH = 179

ilowS = 0
ihighS = 255
ilowV = 0
ihighV = 255

# create trackbars for color change
cv2.createTrackbar('lowH','image2',ilowH,179,callback)
cv2.createTrackbar('highH','image2',ihighH,179,callback)

cv2.createTrackbar('lowS','image2',ilowS,255,callback)
cv2.createTrackbar('highS','image2',ihighS,255,callback)

cv2.createTrackbar('lowV','image2',ilowV,255,callback)
cv2.createTrackbar('highV','image2',ihighV,255,callback)




while(True):
    # grab the frame
    ret, frame = cap.read()

    # get trackbar positions
    ilowH = cv2.getTrackbarPos('lowH', 'image2')
    ihighH = cv2.getTrackbarPos('highH', 'image2')
    ilowS = cv2.getTrackbarPos('lowS', 'image2')
    ihighS = cv2.getTrackbarPos('highS', 'image2')
    ilowV = cv2.getTrackbarPos('lowV', 'image2')
    ihighV = cv2.getTrackbarPos('highV', 'image2')

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_hsv = np.array([ilowH, ilowS, ilowV])
    higher_hsv = np.array([ihighH, ihighS, ihighV])
    mask = cv2.inRange(hsv, lower_hsv, higher_hsv)

    frame = cv2.bitwise_and(frame, frame, mask=mask)

    # show thresholded image
    cv2.imshow('image', frame)
    
    k = cv2.waitKey(1000) & 0xFF # large wait time to remove freezing
    if k == 113 or k == 27:
        break


cv2.destroyAllWindows()
cap.release()
