import cv2, time

video = cv2.VideoCapture('../files/facial_recognition/video.mp4')

a = 0

while True:
    a = a + 1
    check, frame = video.read()

    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Capturing', frame)

    key = cv2.waitKey(40)

    if key == ord('q'):
        break

print(a)
video.release()
cv2.destroyAllWindows()