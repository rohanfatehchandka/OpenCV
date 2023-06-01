import cv2
import numpy as np
##################
widthImg=640
heightImg=480
#####################


frameWidth=640
frameHeight=480
##to use webcam
webcap = cv2.VideoCapture(0)
webcap.set(3, frameWidth) #width has id no.3
webcap.set(4, frameHeight) #height has id no.4
webcap.set(10, 150) #brightness has id 10

def preProcessing(img):
    imgGray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur=cv2.GaussianBlur(imgGray,(5,5),1) #size of kernel is 5*5 and sigma x is 1(scale )
    imgCanny= cv2.Canny(imgBlur,200,200)#numbers are threshold intensity of canny image
    #dilate to make it thick and reode to make it thin
    kernel=np.ones((5,5))
    imgDial= cv2.dilate(imgCanny,kernel,iterations=1)
    imgThres= cv2.erode(imgDial,kernel,iterations=1)
    return imgThres

def getContours(img):
   biggest=np.array([])
   maxArea=0
   contours,hierachy=cv2.findContours(img,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
   for cnt in contours:
      area=cv2.contourArea(cnt)
     # print(area)
      if area>5000:
         #cv2.drawContours(imgContour,cnt,-1,(255,0,0),3)
         peri= cv2.arcLength(cnt,True)
         print(peri)
         #approimate corner points
         #approx is an array of corners
         approx = cv2.approxPolyDP(cnt,0.02*peri,True)
         if  area>maxArea and len(approx)==4:
             biggest=approx
             maxArea=area
   cv2.drawContours(imgContour, biggest, -1, (255, 0, 0), 20)
   return biggest



while True:

    success, img = webcap.read() #success is a boolean
    cv2.resize(img,(widthImg,heightImg))
    imgContour=img.copy()
    imgThres=preProcessing(img)
    getContours(imgThres)
    cv2.imshow("result", imgThres)  #vimg is a series of images in the video
    if cv2.waitKey(1) & 0xFF == ord("q"): #if q is pressed the video stops
        break