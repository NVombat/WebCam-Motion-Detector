import cv2

#Creates a cascade classifier object which allows us to search for a face in an image
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#Using grayscale increases accuracy of finding faces so Convert the image to grayscale
img = cv2.imread("Practice/images/test1.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Use the classifier to detect faces
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5)
print(faces)

#The faces variable is a numpy array with coordinates for the points on the picture where the face will be if connected
for x,y,w,h in faces:
    #Draw a rectangle around the faces and give it a color and width
    img = cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 3)

# # Resize the image to quarter the original size using shape attributeq
# resized_img = cv2.resize(img,(int(img.shape[1]/4), int(img.shape[0]/4)))

cv2.imshow("Detected Face", img)
cv2.waitKey(0)
cv2.destroyAllWindows()