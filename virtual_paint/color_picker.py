import cv2 as cv
import numpy as np

frameWidth = 640
frameHeight = 480
cap = cv.VideoCapture(2)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 130)

def empty(a):
    pass

cv.namedWindow("HSV")
cv.resizeWindow("HSV", 640,220)
cv.createTrackbar("Hue min", "HSV", 30,179,empty)
cv.createTrackbar("Hue max", "HSV", 118,179,empty)
cv.createTrackbar("sat min", "HSV", 0,255,empty)
cv.createTrackbar("sat max", "HSV", 53,255,empty)
cv.createTrackbar("val min", "HSV", 151,255,empty)
cv.createTrackbar("val max", "HSV", 247,255,empty)

while True:
    _, img = cap.read()
    imgHSV =  cv.cvtColor(img, cv.COLOR_BGR2HSV)

    h_min = cv.getTrackbarPos("Hue min", "HSV")
    h_max = cv.getTrackbarPos("Hue max", "HSV")
    s_min = cv.getTrackbarPos("sat min", "HSV")
    s_max = cv.getTrackbarPos("sat max", "HSV")
    v_min = cv.getTrackbarPos("val min", "HSV")
    v_max = cv.getTrackbarPos("val max", "HSV")
    print(h_min,s_min,v_min, h_max, s_max, v_max)
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv.inRange(imgHSV, lower, upper)
    Result = cv.bitwise_and(img, img, mask=mask)

    mask = cv.cvtColor(mask, cv.COLOR_GRAY2BGR)
    hStack = np.hstack([img, mask, Result])
    # cv.imshow("img", img)
    # cv.imshow("HSV", imgHSV)
    # cv.imshow("mask", mask)
    # cv.imshow("result", Result)

    cv.imshow("Horizontal Stacking", hStack)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()