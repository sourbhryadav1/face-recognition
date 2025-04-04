import cv2 as cv

frameWidth = 640
frameHeight = 480
plateCascade  = cv.CascadeClassifier("haar_russian_plates.xml")
minArea = 500
color = (255,0,255)

cap =  cv.VideoCapture(2)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)
while True:
    success, img = cap.read()
    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    numberPlates = plateCascade.detectMultiScale(imgGray, 1.1, 4)
    for (x,y,w,h) in numberPlates:
        area = w*h
        if area > minArea:
            cv.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
            cv.putText(img, "Number Plate", (x,y-5), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)
            imgRoi = img[y:y+h, x:x+w]
            cv.imshow("ROI", imgRoi)

    cv.imshow("img", img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break