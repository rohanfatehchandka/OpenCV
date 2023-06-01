import cv2
import numpy as np

img = cv2.imread(r"C:\Users\rohan\PycharmProjects\pythonProject1\OpenCvPython\Resources\cards.jpg")

width,height = 250,350
pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]])  # getting coordinates from paint
# pts1 = np.float32([[278,119],[451,134],[280,367],[451,368]])  # getting coordinates from paint

pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]]) # defining the order of our points
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))


cv2.imshow("Image",img)
cv2.imshow("Output",imgOutput)

cv2.waitKey(0)