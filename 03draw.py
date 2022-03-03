# # blank image
import cv2 as cv
import numpy as np
blank=np.zeros((500,500), dtype = 'uint8')
cv.imshow('Blank',blank)
cv.waitKey(0)

#paint a particular color
import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3), dtype = 'uint8')

blank[:]= 0,255,0  # RGB 
#we can put dimensions to paint a paticular part.

cv.imshow('Green',blank)
cv.waitKey(0)


#drawing a rectangle/square
import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3), dtype = 'uint8')

cv.rectangle(blank,(100,100),(400,400),(0,255,0),thickness=3) # use thickness=cv.FILLED [or] thickeness= -1 to fill the rectangle with color.
#changing the dimensions in above code block will make the shape a rectangle or a square.

cv.imshow('Rectangle',blank)
cv.waitKey(0)

#drawing a circle
import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3), dtype = 'uint8')

cv.circle(blank,(250,250),50,(0,0,255),thickness=4) # use thickness=cv.FILLED [or] thickeness= -1 to fill the rectangle with color.
cv.imshow('Circle',blank)
cv.waitKey(0)

#drawing a circle
import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3), dtype = 'uint8')
cv.line(blank,(100,100),(100,300),(255,0,0),thickness=3)
cv.imshow('Line',blank)
cv.waitKey(0)

#text on image
import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3), dtype = 'uint8')
cv.putText(blank,'Hello, My name is Ayush',(0,225),cv.FONT_HERSHEY_TRIPLEX,1.0,(255,0,0),thickness=3)
cv.imshow('Text',blank)
cv.waitKey(0)