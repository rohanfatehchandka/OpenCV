import cv2
import numpy as np

img = cv2.imread(r"C:\Users\rohan\PycharmProjects\pythonProject1\OpenCvPython\Resources\download (1).jpg")
kernel = np.ones((5, 5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)         #Convert to gray colour (BGR to Grey means RGB to gray)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)   # 2nd arg is odd(kernel) and 3rd is known as sigma x
imgCanny = cv2.Canny(img, 150, 200)          # To get out lines higher the value lesser the outlines(better)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)   #To increase thickness of out-lines iteration tells the thickness
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)   #To decrease thickness of outlines

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialation Image", imgDialation)
cv2.imshow("Eroded Image", imgEroded)
cv2.waitKey(0)