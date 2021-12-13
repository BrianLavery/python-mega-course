import cv2, time

# Variable for first frame - remains as a static value
first_frame = None # Use this to create a variable but not assign a value

# video = cv2.VideoCapture(0)
video = cv2.VideoCapture('./files/video.mp4')

while True:
    check, frame = video.read()

    frame = cv2.resize(frame, (int(frame.shape[1] / 3), int(frame.shape[0] / 3)))

    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    grey = cv2.GaussianBlur(grey,(21,21),0) # Want to add blur to smooth noise; pass in a tuple as size of blur. Last number is StD.

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
        if cv2.contourArea(contour) < 1000:
            continue

        (x, y, w, h) = cv2.boundingRect(contour) # Create rectangle for big changes
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1) # Draw rectangle

    cv2.imshow('Grey Frame', frame)
    cv2.imshow('Delta Frame', delta_frame)
    cv2.imshow('Threshold Frame', thresh_frame)

    key = cv2.waitKey(40)
    print(grey)
    print(delta_frame)

    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()