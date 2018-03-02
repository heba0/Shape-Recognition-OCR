from YellowShapeDetector import ShapeDetectorYellow
import numpy as np
import imutils
import cv2

cap = cv2.VideoCapture(0)
##yellow
##ilowH = 4
##ihighH = 73
##
##ilowS = 8
##ihighS = 185
##ilowV = 194
##ihighV = 255

#black
##ilowH = 99
##ihighH = 117
##
##ilowS = 0
##ihighS = 255
##ilowV = 0
##ihighV = 255

#Red
##ilowH = 141
##ihighH = 179
##
##ilowS = 0
##ihighS = 255
##ilowV = 0
##ihighV = 255


#Red2
ilowH = 142
ihighH = 179

ilowS = 58
ihighS = 183
ilowV = 100
ihighV = 255


#white
##ilowH = 95
##ihighH = 123
##
##ilowS = 23
##ihighS = 180
##ilowV = 108
##ihighV = 177

##yellow2
##ilowH = 5
##ihighH = 68
##
##ilowS = 23
##ihighS = 255
##ilowV = 144
##ihighV = 169

#Morphology Kernels
kernelOpen=np.ones((10,10))
kernelClose=np.ones((20,20))
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    #cv2.imshow('camera',frame)
    resized = imutils.resize(frame, width=300)
    ratio = frame.shape[0] / float(resized.shape[0])

    # Our operations on the frame come here
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_hsv = np.array([ilowH, ilowS, ilowV])
    higher_hsv = np.array([ihighH, ihighS, ihighV])
    mask = cv2.inRange(hsv, lower_hsv, higher_hsv)
    maskOpen=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernelOpen)
    maskClose=cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelClose)

    frame = cv2.bitwise_and(frame, frame, mask=maskClose)    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #print("1")
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
    # find contours in the thresholded image
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_TREE,
            cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    sd = ShapeDetectorYellow()
   # cv2.imshow('frame',gray)
    cv2.imshow('frameYellow',frame)
    # loop over the contours
    for c in cnts:
        # compute the center of the contour
        M = cv2.moments(c)
        if(M["m00"]>0):
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            shape = sd.detect(c)
            
            # multiply the contour (x, y)-coordinates by the resize ratio,
            # then draw the contours and the name of the shape on the image
            c = c.astype("float")
            c *= ratio
            c = c.astype("int")
            cv2.drawContours(gray, [c], -1, (0, 255, 0), 2)
            cv2.putText(gray, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
		0.5, (255, 0, 255), 2)
            # Display the resulting frame
            cv2.imshow('frame', gray)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
cap.release()
cv2.destroyAllWindows()

# When everything done, release the capture
#sources
#https://www.pyimagesearch.com/2016/02/08/opencv-shape-detection/
#https://thecodacus.com/opencv-object-tracking-colour-detection-python/#.Woubt6iWY2w
