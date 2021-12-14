import cv2
import glob
import os.path

# Produces relative path of files
images = glob.glob("./files/sample_images/*.jpg")

for image in images:
    img = cv2.imread(image, 0)
    resized_img = cv2.resize(img, (100, 100))
    cv2.imwrite("./files/sample_images/resized_images/" + os.path.basename(image), resized_img) # basename gets just the filename