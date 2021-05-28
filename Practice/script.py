#Import libraries
import cv2

#Read image file into n dimensional numpy array
#Read as greyscale image -> 0, Read as color image w/o transparency -> 1, Read as color image w transparency -> -1
img = cv2.imread("Practice/images/galaxy.jpg", 0)

print(type(img))
print(img)

#To know the number of rows and columns
print(img.shape)
#To know the number of dimensions
print(img.ndim)

#Resize image to certain dimensions (width, height)
#resized_img = cv2.resize(img,(500,900))

#Resize the image to half the original size using shape attribute
resized_img = cv2.resize(img,(int(img.shape[1]/2), int(img.shape[0]/2)))

#Display image on screen
#cv2.imshow("Galaxy", img)
cv2.imshow("Galaxy", resized_img)
#Amount of time (in milliseconds) before window closes (0 -> closes window on key/button press)
cv2.waitKey(0)
#Remove all windows
cv2.destroyAllWindows()

#Write new image to jpg file
cv2.imwrite("Practice/images/galaxy_resized.jpg", resized_img)