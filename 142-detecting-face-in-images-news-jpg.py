import cv2

# Load facial detection cascade
face_cascade = cv2.CascadeClassifier('./files/facial_recognition/haarcascade_frontalface_default.xml')

# Load image to search for face - default is use colour image
img = cv2.imread('./files/facial_recognition/news.jpg')

# Want to grayscale when look for face - improves accuracy - do with a method
grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Search for cascade and return coordinates of image
# Will be upper left point of face as well and also return height and width of face

faces = face_cascade.detectMultiScale(grey_img,
scaleFactor = 1.1, # Use 1.1 scale here to get rid of hand
minNeighbors = 5) # Neighbours related to how many faces around

print(type(faces))
print(faces) # [[157  84 379 379]]
# Starting height, starting width, then size

# Can draw a rectangle
# Pass starting coordinates and end coordinates to it for second parameter
# Next parameter is colour of rectangle
# Next parameter is width of rectangle
for x, y, w, h in faces:
    img = cv2.rectangle(img, (x,y),(x + w, y + h), (0, 255, 0), 2)

# Resize image in case bigger than screen
# resized = cv2.resize(img, (int(img.shape[1] / 3), int(img.shape[0] / 3)))

# Show image
cv2.imshow('Grey', img)
cv2.waitKey(0)
cv2.destroyAllWindows()