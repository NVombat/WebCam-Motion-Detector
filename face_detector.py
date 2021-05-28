#Import libraries
import cv2

#Creates a cascade classifier object which allows us to search for a face in an image
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#Using grayscale increases accuracy of finding faces
#Read image using cv2 library
img = cv2.imread("Practice/images/news.jpg")
#Convert the image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Use the classifier to detect faces
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5)
print(faces)

#The faces variable is a numpy array with coordinates for the points on the picture where the face will be if connected
for x,y,w,h in faces:
    #Draw a rectangle around the faces and give it a color and width
    img = cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 3)

#Show the image with the rectangle
cv2.imshow("Detected Face", img)
cv2.waitKey(0)
cv2.destroyAllWindows()