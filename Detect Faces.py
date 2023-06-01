import cv2

faceCascade= cv2.CascadeClassifier(r"C:\Users\rohan\PycharmProjects\pythonProject1\OpenCvPython\Resources\haarcascade_frontalface_default.xml")  # Create object of our trained model
img = cv2.imread(r'C:\Users\rohan\PycharmProjects\pythonProject1\OpenCvPython\Resources\lena.png')
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray,1.1,4)         # Face detection on gray image

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)


cv2.imshow("Result", img)
cv2.waitKey(0)