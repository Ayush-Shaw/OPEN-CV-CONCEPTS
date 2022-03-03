#reshaping resizing video

import cv2 as cv

def rescaleFrame(frame,scale=0.2):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)

    return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)
    
video = cv.VideoCapture(r"C:/Users/Ayush Shaw/Downloads/S video.mp4")
while True:
    isTrue, frame= video.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow('Sukku', frame)

    cv.imshow('SukkuResized',frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

video.release()
cv.destroyAllWindows()

#resizing reshaping images
import cv2 as cv

def rescaleFrame(frame,scale=0.2):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)

    return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)

img=cv.imread(r"D:/PROJECTS  SELFWORK/Project DSA/10 A/Ronaldo.jpg")
cv.imshow('img1', img)

resized_img = rescaleFrame(img)
cv.imshow('img_resized',resized_img)

cv.waitKey(10000)
cv.destroyAllWindows()