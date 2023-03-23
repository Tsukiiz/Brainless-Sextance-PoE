import cv2 as cv
import numpy as np

poeImg = cv.imread('realtest.jpg', cv.IMREAD_UNCHANGED)
needleImg = cv.imread('object.jpg', cv.IMREAD_UNCHANGED)

result = cv.matchTemplate(poeImg, needleImg, cv.TM_CCOEFF_NORMED)

minVal, maxVal, minLoc, maxLoc = cv.minMaxLoc(result)

print(maxLoc)
print(maxVal)

needleW = needleImg.shape[1]
needleH = needleImg.shape[0]

topLeft = maxLoc
bottomRight = (topLeft[0] + needleW, topLeft[1] + needleH)

cv.rectangle(poeImg, topLeft, bottomRight, color=(0,255,0), thickness=2, lineType=cv.LINE_4)
cv.imwrite('result',poeImg)
# cv.imshow('result', poeImg)
# cv.waitKey()