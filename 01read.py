#reading images

import cv2 as cv
img=cv.imread(r"D:/PROJECTS  SELFWORK/Project DSA/10 A/Ronaldo.jpg")
cv.imshow('img1', img)
cv.waitKey(10000)
cv.destroyAllWindows()

#reading videos
video = cv.VideoCapture(r"C:/Users/Ayush Shaw/Downloads/S video.mp4")
while True:
    isTrue, frame= video.read()

    cv.imshow('Sukku', frame)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

video.release()
cv.destroyAllWindows()