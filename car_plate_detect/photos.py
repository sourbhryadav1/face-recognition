import cv2 as cv

frameWidth = 640
frameHeight = 480
plateCascade  = cv.CascadeClassifier("haar_russian_plates.xml")
minArea = 500
color = (255,0,255)

def rescaleFrame(frame, scale=0.3):
    """
    works for images, videos, and live videos
    """
    width = int(frame.shape[1]*scale) # frame.shape[1] = width, and shape[0] = height
    height = int(frame.shape[0]*scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread(r"C:\Desktop\_\programming\ML\ML code\opencv\car_plate_detect\personalized-car-number-plate-BJ1DMN.jpg")
while True:
    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    numberPlates = plateCascade.detectMultiScale(imgGray, 1.1, 4)
    for (x,y,w,h) in numberPlates:
        area = w*h
        if area > minArea:
            cv.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
            cv.putText(img, "Number Plate", (x,y-5), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)
            imgRoi = img[y:y+h, x:x+w]
            cv.imshow("Roi", imgRoi)

    cv.imshow("img", img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break