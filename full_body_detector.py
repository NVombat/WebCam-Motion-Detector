import numpy as np
import cv2

#Creates a cascade classifier object which allows us to search for a full body in an image
full_body_cascade = cv2.CascadeClassifier('/home/nvombat/Desktop/WebCam-Motion-Detector/haarcascade_fullbody_default.xml')

img = cv2.imread("Practice/images/people2.jpg")
#print(type(img))
#print(img)

# Resize the image to quarter the original size
resized_img = cv2.resize(img,(int(img.shape[1])/4, int(img.shape[0]/4)))

#Convert the image to grayscale
gray_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY) 
#print(gray_img)

#Use the classifier to detect bodies
bodies = full_body_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=0)
#print(type(bodies))
#print(bodies)

#The bodies variable is a numpy array with coordinates for the points on the picture where the body will be if connected
for (x,y,w,h) in bodies:
    #Draw a rectangle around the bodies and give it a color and width
    resized_img = cv2.rectangle(resized_img, (x,y), (x+w,y+h), (0,255,255), 10)

# Resize the image to quarter the original size
# resized_img = cv2.resize(img,(int(img.shape[1]/4), int(img.shape[0]/4)))
#resized_img = cv2.resize(img, (100,100))

cv2.imshow('Detected Bodies',resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()