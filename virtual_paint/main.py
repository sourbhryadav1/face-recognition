import cv2 as cv
import numpy as np

frameWidth = 640
frameHeight = 480
cap = cv.VideoCapture(2)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 130)

myColors = [[62, 58, 140, 74, 255, 255],
            [97, 25, 79, 139, 158, 149]]

myColorVal = [[51, 255, 51],
              [148, 184, 184]]

myPoints = []  # x,y,colorID


def find_color(img, myColors, myColorVal):
    imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    count = 0
    newPoints = []
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv.inRange(imgHSV, lower, upper)
        x, y = getContours(mask)
        cv.circle(imgResult, (x, y), 10, myColorVal[count], cv.FILLED)
        if x != 0 and y != 0:
            newPoints.append([x, y, count])
        count += 1
    return newPoints


def getContours(img):
    contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv.contourArea(cnt)
        if area > 500:
            peri = cv.arcLength(cnt, True)
            approx = cv.approxPolyDP(cnt, 0.02 * peri, True)
            x, y, w, h = cv.boundingRect(approx)
    return x + w // 2, y


def drawOnCanvas(myPoints, myColorVal):
    for points in myPoints:
        cv.circle(imgResult, (points[0], points[1]), 10, myColorVal[points[2]], cv.FILLED)


while True:
    success, img = cap.read()
    if not success:
        break

    img = cv.flip(img, 1)  # Flip the image horizontally (mirroring effect)
    imgResult = img.copy()

    newPoints = find_color(img, myColors, myColorVal)
    if len(newPoints) != 0:
        for newP in newPoints:
            myPoints.append(newP)

    if len(myPoints) != 0:
        drawOnCanvas(myPoints, myColorVal)

    cv.imshow("Mirrored Result", imgResult)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()