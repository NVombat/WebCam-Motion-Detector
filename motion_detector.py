#Import libraries
from datetime import datetime as dt
import cv2, time
import pandas

first_frame = None
#Keeps track of the status and switches in state
status_list = [None, None]
#Records times of changes of state
time_list = []

#Create a dataframe to store the time values
df = pandas.DataFrame(columns=['Start', 'End'])

#Captures video and stores it in variable
#Argument can be path to a video file or 0,1,2... for the ith camera on your device
#Triggers Camera
video = cv2.VideoCapture(0)

while True:
    #Capture frame from webcam (frame is a numpy array)
    check, frame = video.read()
    # print(check)
    # print(frame)

    #Status checks if there is a change of state -> object in motion or not
    status=0
    #Convert the frame to grayscale and blur it
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame = cv2.GaussianBlur(gray_frame,(21,21),0)

    #Receives the first frame of the video and skips to next frame
    if first_frame is None:
        first_frame = gray_frame
        continue

    #Difference between first and current frame
    delta_frame = cv2.absdiff(first_frame, gray_frame)
    #Sets a threshold and specifies threshold limit (30) -> white color to those that exceed threshold limit(255)
    #threshold returns a tuple -> access second value of tuple which is actual frame 
    threshold_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    #Smoothens the image
    threshold_frame = cv2.dilate(threshold_frame, None, iterations=2)

    #Find all contours of the distinct objects in the image
    (cntrs,_) = cv2.findContours(threshold_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    #Filter out the contours -> Keep only specific values
    for contour in cntrs:
        #Filter by area of contour
        if cv2.contourArea(contour) < 10000:
            continue
        #Change status to 1 as soon as an object enters the screen
        status=1
        #If area of contour is satisfied then it is an object that is moving
        #Get its dimensions
        (x,y,w,h) = cv2.boundingRect(contour)
        #Use dimensions to draw the rectangle on these objects
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)

    #Add status to status list
    status_list.append(status)
    #Saves memory by appending only the last two items to the list
    status_list = status_list[-2:]

    #Recording time when state changes from motion to no motion
    if status_list[-1] == 1 and status_list[-2] == 0:
        time_list.append(dt.now())
    #Records time when state changes from no motion to motion
    if status_list[-1] == 0 and status_list[-2] == 1:
        time_list.append(dt.now())

    #Display the frames in a window
    cv2.imshow("Gray Frame", gray_frame)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Threshold Frame", threshold_frame)
    cv2.imshow("Bounding Rectangle", frame)

    # print(gray)
    # print(delta_frame)
    # print(thresh_frame)

    #Quit the window if user presses q
    key = cv2.waitKey(1)
    if key == ord('q'):
        if status == 1:
            time_list.append(dt.now())
        break

# print(status_list)
# print(time_list)

#Fill dataframe
for i in range(0, len(time_list), 2):
    df = df.append({"Start": time_list[i], "End": time_list[i+1]}, ignore_index=True)

#Write the dataframe containing timestamps to a csv file
df.to_csv("times.csv", mode='a', header=False)

video.release()
cv2.destroyAllWindows()


#TO READ CSV FILE AND MAKE SURE INDEXING IS CORRECT
# df = pandas.read_csv('times.csv')
# df.drop('Unnamed: 0', axis='columns', inplace=True)
# print(df['Start'], df['End'], df)