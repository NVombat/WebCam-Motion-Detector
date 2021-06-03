#USING HOG DESCRIPTOR -> Histogram of Oriented Gradients 
import cv2
import numpy as np

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
#Enables webcam and starts recording
vid=cv2.VideoCapture(0)
while True:
    #Record video frame by frame
    check,frame = vid.read()
    #Detects objects of different sizes
    f,w=hog.detectMultiScale(frame, winStride=(8,8), padding=(32,32), scale=1.05)
    
    #Draw a rectangle around the bodies
    for (x,y,w,h) in f:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,255), 3)
        
    #Display the frame in a window
    cv2.imshow('Body',frame)
    #Quit the window if user presses q
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

#This makes sure the camera is released
vid.release()
#Destroy the display window
cv2.destroyAllWindows()