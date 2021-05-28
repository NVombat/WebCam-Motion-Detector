#Import libraries
from pathlib import Path
import glob
import cv2

#Fetches all files from the images folder with a .jpg extension
images = glob.glob("Practice/images/*.jpg")
#Extracts the name of the file from the entire path
#images = [Path(filename).name for filename in images]
#print(images)

#Runs through each the image files
for image in images:
    #Reads the image in a greyscale format
    img = cv2.imread(image,0)
    #print(img)
    #Resizes the image to 100x100
    resized_img = cv2.resize(img,(100,100))
    #Displays the resized image
    cv2.imshow("Resized",resized_img)
    #Displays the image for 2 seconds
    cv2.waitKey(2000)
    #Destroys the window
    cv2.destroyAllWindows()
    #Extracts name of file from file path
    img_name = Path(image).name
    #print(img_name)
    #Writes the resized image to the folder as a jpg file
    cv2.imwrite("Practice/images/resized_"+img_name,resized_img)