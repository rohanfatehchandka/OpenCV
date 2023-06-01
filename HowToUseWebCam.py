import cv2

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)      # 0 for web cam
cap.set(3, frameWidth)   # channel 3 is for width
cap.set(4, frameHeight)  # channel 4 is for height
cap.set(10, 150)         # channel 10 is for brightness
while True:
    success, img = cap.read()
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):       #To switch off the cam
        break