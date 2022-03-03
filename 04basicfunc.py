import cv2 as cv
img = cv.imread(r"D:\PROJECTS  SELFWORK\Project DSA\10 A\Messi.jpg")
cv.imshow('Messi',img)
cv.waitKey(0)
cv.destroyAllWindows()


# Converting to Grayscale

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('GrayscaleImg',gray)
cv.waitKey(0)
cv.destroyAllWindows()


# Blur an image

blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)
cv.waitKey(0)
cv.destroyAllWindows()

# Edge cascade - finding edges in the image

canny = cv.Canny(img,150,250)
cv.imshow('CannyImg',canny)
cv.waitKey(0)
cv.destroyAllWindows()

# Dilating the image

dilated = cv.dilate(canny,(7,7),iterations=3)
cv.imshow('DilatedImg',dilated)
cv.waitKey(0)
cv.destroyAllWindows()

# Eroding

eroded=cv.erode(dilated,(7,7),iterations=3)
cv.imshow('Eroded',eroded)
cv.waitKey(0)
cv.destroyAllWindows()

# Reszie / Crop Image

resized=cv.resize(img,(100,200),interpolation=cv.INTER_AREA) # cv.INTER_AREA is used to shrink an image , cv.INTER_LINEAR or cv.INTER_CUBIC is used to enlarge the image.
cv.imshow('Resized',resized)
cv.waitKey(0)
cv.destroyAllWindows()

# Cropping

cropped= img[50:200,200:400]
cv.imshow('Cropped',cropped)
cv.waitKey(0)
cv.destroyAllWindows()

