import cv2 as cv
import numpy as np
img =cv.imread(r"D:\PROJECTS  SELFWORK\Project DSA\10 A\Messi.jpg")
cv.imshow('Messi',img)

# Translation - Shifitng an image about x and y axis

def translate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]]) # if -x then shift towards left and -y implies shift upwards
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)

translated = translate(img,100,100) 
cv.imshow('Translated',translated)
cv.waitKey(0)
cv.destroyAllWindows()

# Rotation
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width,height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -45) #for anticlockwise make it positive
cv.imshow('Rotated', rotated)

rotated_rotated = rotate(img, -90)
cv.imshow('Rotated Rotated', rotated_rotated)
cv.waitKey()
cv.destroyAllWindows()

# Flipping
flip = cv.flip(img, -1) #can be 0 (flip vertically) and 1 (horizontal flip) and -1 flips is both vertically and horizontally
cv.imshow('Flip', flip)
cv.waitKey(0)
cv.destroyAllWindows()

#Cropping
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)
cv.waitKey(0)
cv.destroyAllWindows()
    