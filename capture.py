#Import libraries
import cv2

first_frame = None

#Captures video and stores it in variable
#Argument can be path to a video file or 0,1,2... for the ith camera on your device
#Triggers Camera
video = cv2.VideoCapture(0)

while True:
    #Capture frame from webcam (frame is a numpy array)
    check, frame = video.read()
    # print(check)
    # print(frame)

    #Convert the frame to grayscale and blur it
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(21,21),0)

    #Receives the first frame of the video and skips to next frame
    if first_frame is None:
        first_frame = gray
        continue

    #Difference between first and current frame
    delta_frame = cv2.absdiff(first_frame, gray)
    #Sets a threshold and specifies threshold limit (30) -> white color to those that exceed threshold limit(255)
    #threshold returns a tuple -> access second value of tuple which is actual frame 
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    #Smoothens the image
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    #Find all contours of the distinct objects in the image
    (cnts,_) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    #Filter out the contours -> Keep only specific values
    for contour in cnts:
        #Filter by area of contour
        if cv2.contourArea(contour) < 1000:
            continue
        #If area of contour is satisfied then it is an object that is moving
        #Get its dimensions
        (x,y,w,h) = cv2.boundingRect(contour)
        #Use dimensions to draw the rectangle on these objects
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)

    #Display the frames in a window
    cv2.imshow("Gray Frame", gray)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Threshold Frame", thresh_frame)
    cv2.imshow("Bounding Rectangle", frame)

    # print(gray)
    # print(delta_frame)
    # print(thresh_frame)

    #Quit the window if user presses q
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

#This makes sure the camera is released
video.release()
#Destroy the display window
cv2.destroyAllWindows()