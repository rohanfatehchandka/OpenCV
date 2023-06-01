import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)    # 512 by 512 is row and column of our matrix which in turn means it is the pixels for our img and 3 is no of channel for BGR i.e Colour
#print(img)
img[:]= 255,0,0     #convert img to blue .....(:) signifies whole img

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3) # Start point and end point of diagaonals(x,y) system ,color,thickness
cv2.rectangle(img,(0,0),(250,350),(0,0,255),2)  #same as above
cv2.circle(img,(400,50),30,(255,255,0),5)   #Start point and radius
cv2.putText(img," OPENCV  ",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),3)   # start point,text,font face,scale,color,thickness

# These all functions overwrite original image so no need to copy in new one


cv2.imshow("Image",img)

cv2.waitKey(0)