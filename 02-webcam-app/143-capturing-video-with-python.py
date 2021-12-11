import cv2, time

# Trigger a video capture object - takes argument as number or video file path
# If i have multiple video cameras they each get a number starting from 0
# For video on hard drive need the path to the video file
# video = cv2.VideoCapture(0)
video = cv2.VideoCapture('./files/video.mp4')

# Create a while loop here for multiple frames
while True:
    # Create a frame object to display images from video
    check, frame = video.read()

    # print(check)
    # print(frame)

    # Convert frame to grayscale
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # time.sleep(3)

    # We show the image frame(s)
    cv2.imshow('Capturing', frame)

    # My wait key
    key = cv2.waitKey(40)

    # Allows you to enter a command to break the loop
    if key == ord('q'):
        break

# Use this method to release the video
video.release()
cv2.destroyAllWindows()