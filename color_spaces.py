import cv2 as cv #shows pictures in BGR format
import matplotlib.pyplot as plt

img = cv.imread(r"D:\\PROJECTS  SELFWORK\\Project DSA\\10 A\\Gareth bale.jpg")
cv.imshow('Player', img)

plt.imshow(img)
plt.show()

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to L*a*b [or] LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# We can convert the opposite of the 4 mentioned above i.e Grayscale to BGR , HSV to BGR , L*a*B to BGR , RGB to BGR.
# But we can cannot directly convert from Grayscale to HSV , HSV to LAB etc etc.
# HSV to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('LAB --> BGR', lab_bgr)

cv.waitKey(0)