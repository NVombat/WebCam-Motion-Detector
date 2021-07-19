#REF - https://towardsdatascience.com/computer-vision-for-beginners-part-4-64a8d9856208

#Import libraries RUN USING RUN BUTTON
from datetime import datetime as dt
import cv2, time, pandas

img = cv2.imread("Practice/images/face.jpg")
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# cv2.imshow("Face", img)

#Blur image to reduce distortion
blurred_img = cv2.bilateralFilter(img, d = 7, sigmaSpace = 75, sigmaColor =75)
#Grayscale conversion
gray_img = cv2.cvtColor(blurred_img, cv2.COLOR_RGB2GRAY)
#Threshold values and image display
a = gray_img.max()  
_, frame = cv2.threshold(gray_img, a/2+60, a,cv2.THRESH_BINARY_INV)
#cv2.imshow("Gray", frame)

#Find contours
img, cntrs, hrchy = cv2.findContours(image = frame, mode = cv2.RETR_TREE, method = cv2.CHAIN_APPROX_SIMPLE)
cntrs = sorted(cntrs, key = cv2.contourArea, reverse = True)
#Draw the contour 
img_cntr = img.copy()
final = cv2.drawContours(img_cntr, cntrs, contourIdx = -1, color = (255, 0, 0), thickness = 2)
# cv2.imshow("Contours", img_cntr)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
# Detect the convex contour
c_0 = cntrs[0]
hull = cv2.convexHull(c_0)
img_copy = img.copy()
img_hull = cv2.drawContours(img_copy, contours = [hull], 
                            contourIdx = 0, 
                            color = (255, 0, 0), thickness = 2)
cv2.imshow("Hull", img_hull)
cv2.waitKey(0)
cv2.destroyAllWindows()