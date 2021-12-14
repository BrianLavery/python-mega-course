import cv2

# Second parameter is how to read image
# a = RGB (1) / B&W (0) / RGBA (-1) allowing transparency
img = cv2.imread("./files/galaxy.jpg", 0)

print(type(img))
print(img)
print(img.shape) # Gives resolution
print(img.ndim) # Gives dimenions in array, would be different if RGB

# Can resize image
# Pass the new dimensions as a tuple
# Python is combining values in the numpy array
resized_image = cv2.resize(img, (1000, 500))

# To keep aspect ratio
same_aspect_image = cv2.resize(img, (int(img.shape[1] / 2), int(img.shape[0] / 2)))

# Allows to display image. Galaxy is the name of the window
cv2.imshow("Galaxy", img) 
cv2.imshow("Galaxy2", resized_image)
cv2.imshow("Galaxy3", same_aspect_image)

# cv2.waitKey(0) # Allows user to close window with a 0
cv2.waitKey(5000) # Means window closes in 5 seconds

cv2.destroyAllWindows() # What to do after waitKey

# Output image
cv2.imwrite("./files/Galaxy_resized.jpg", same_aspect_image)