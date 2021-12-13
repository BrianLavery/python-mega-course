import cv2, pandas
from datetime import datetime

# Variable for first frame - remains as a static value
first_frame = None # Use this to create a variable but not assign a value
status_list = [None, None] # Use this to record statuses
times = []
df = pandas.DataFrame(columns = ["Start", "End"])

# video = cv2.VideoCapture(0)
video = cv2.VideoCapture('./files/video.mp4')

while True:
    check, frame = video.read()
    status = 0 # This is to enable storage of times object enters frame
    frame = cv2.resize(frame, (int(frame.shape[1] / 3), int(frame.shape[0] / 3)))
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    grey = cv2.GaussianBlur(grey,(21,21), 0) # Want to add blur to smooth noise; pass in a tuple as size of blur. Last number is StD.

    if first_frame is None: # Only assign first frame once
        first_frame = grey
        continue # Ensures everything below this line in while loop won't run
    
    delta_frame = cv2.absdiff(first_frame, grey)

    # Set a threshold to make things either return black or white
    # Anything 30 or above becomes white
    # Threshold method returns a tuple and we only need second item
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations = 2) # None parameter relates to a kernel array

    # Want to find contours
    # Store result in a tuple and make a copy of frame to do it
    (cnts,_) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Want to keep contours only bigger than 1000 pixels
    for contour in cnts:
        if cv2.contourArea(contour) < 10000:
            continue
        status = 1 # Mark where we do have a large contour
        (x, y, w, h) = cv2.boundingRect(contour) # Create rectangle for big changes
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1) # Draw rectangle

    status_list.append(status)

    # Compare last two items of the list
    if status_list[-1] == 1 and status_list[-2] == 0:
        times.append(datetime.now())
    if status_list[-1] == 0 and status_list[-2] == 1:
        times.append(datetime.now())

    cv2.imshow('Grey Frame', grey)
    cv2.imshow('Delta Frame', delta_frame)
    cv2.imshow('Threshold Frame', thresh_frame)
    cv2.imshow('Colour Frame', frame)

    key = cv2.waitKey(40)

    if key == ord('q'):
        if status == 1:
            times.append(datetime.now()) # Append another time in case there is an item in frame
        break
print(status_list)
print(times)

# Iterate through times list to put in pandas data frame
for i in range(0, len(times), 2): # Iterate with step of 2
    df = df.append({"Start": times[i], "End": times[i + 1]}, ignore_index = True)

df.to_csv("./files/times.csv")

video.release()
cv2.destroyAllWindows