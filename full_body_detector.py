#Import libraries
import numpy as np
import cv2

#Creates a cascade classifier object which allows us to search for a full body in an image
full_body_cascade = cv2.CascadeClassifier('/home/nvombat/Desktop/WebCam-Motion-Detector/haarcascade_fullbody_default.xml')

#Read image using cv2 library
img = cv2.imread("Practice/images/people1.jpg")
#print(type(img))
#print(img)
#Convert the image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
#print(gray_img)

#Use the classifier to detect bodies
bodies = full_body_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=3)
#print(type(bodies))
#print(bodies)

#The bodies variable is a numpy array with coordinates for the points on the picture where the body will be if connected
for (x,y,w,h) in bodies:
    #Draw a rectangle around the bodies and give it a color and width
    img = cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,255), 10)

# Resize the image to quarter the original size using shape attribute
resized_img = cv2.resize(img,(int(img.shape[1]/4), int(img.shape[0]/4)))
#resized_img = cv2.resize(img, (100,100))

#Show the image with the rectangle
cv2.imshow('Detected Bodies',resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#HOG DESCRIPTOR
# hog = cv2.HOGDescriptor()
# hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
# vid=cv2.VideoCapture(0)
# while True:
#     check,frame = vid.read()
#     f,w=hog.detectMultiScale(frame, winStride=(8,8), padding=(32,32), scale=1.05)
    
#     for (x,y,w,h) in f:
#         cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,255), 3)
#     #Display the frame in a window
#     cv2.imshow('Body',frame)
#     #Quit the window if user presses q
#     key = cv2.waitKey(1)
#     if key == ord('q'):
#         break

# #This makes sure the camera is released
# vid.release()
# #Destroy the display window
# cv2.destroyAllWindows()