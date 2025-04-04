import cv2 as cv
import numpy as np

frameWidth = 640
frameHeight = 480
cap = cv.VideoCapture(2)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 50)

widthImg, heightImg = 640,480

def preprocessing(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    imgThresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
    return imgThresh


def getContours(img):
    biggest = np.array([])
    maxArea = 0
    contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv.contourArea(cnt)
        if area > 100:
            # cv.drawContours(imgContour, cnt, -1, (255,0,0), 3)
            peri = cv.arcLength(cnt, True)
            approx = cv.approxPolyDP(cnt, 0.02*peri, True)
            if area > maxArea and len(approx) == 4:
                biggest = approx
                maxArea = area
                break
    cv.drawContours(imgContour, biggest, -1, (255,0,0), 20)
    # print(biggest)
    return biggest

# making pts1 and pts2 similar
def reorder(myPoints):
    myPoints = myPoints.reshape((4,2)) #should be in same shape as biggest
    myPointsNew = np.zeros((4,1,2), np.int32)
    add = myPoints.sum(1)
    # print("Add", add)

    myPointsNew[0] = myPoints[np.argmin(add)]
    myPointsNew[3] = myPoints[np.argmax(add)]
    diff = np.diff(myPoints, axis=1)
    myPointsNew[1] = myPoints[np.argmin(diff)]
    myPointsNew[2] = myPoints[np.argmax(diff)]
    # print("New pts", myPointsNew)
    return myPointsNew

def getWarp(img, biggest):
    if biggest.size == 0:
        print("No valid contour detected")
        return img  # Return the original image to avoid crashing
    biggest = reorder(biggest)
    pts1 = np.float32(biggest)
    pts2 = np.float32([[0, 0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]])
    matrix = cv.getPerspectiveTransform(pts1, pts2)
    image_out = cv.warpPerspective(img, matrix, (widthImg, heightImg))
    return image_out

while True:
    success, img = cap.read()
    cv.resize(img, (widthImg, heightImg))
    imgContour = img.copy()
    imgThresh = preprocessing(img)
    biggest = getContours(imgThresh)
    # print(biggest)
    imgWarped = getWarp(img, biggest)

    cv.imshow("input", img)
    cv.imshow("Contour", imgContour)
    cv.imshow("Threshold", imgThresh)
    cv.imshow("Result", imgWarped)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break