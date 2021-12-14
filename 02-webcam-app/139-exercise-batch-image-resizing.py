import cv2

img1 = cv2.imread("./files/sample_images/galaxy.jpg")

resized_img1 = cv2.resize(img1, (100, 100))

cv2.imwrite("./files/sample_images/resized_galaxy.jpg", resized_img1)