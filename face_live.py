import cv2 as cv
import numpy as np
import os

haar_cascade = cv.CascadeClassifier("haar_face.xml")
if haar_cascade.empty():
    print("Error loading haar_face.xml")
    exit()

people = ["me", "harshit", "ansh"]

if not os.path.exists("face_trained.yml"):
    print("Error")
    exit()

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read("face_trained.yml")

# Open webcam
cap = cv.VideoCapture(2)

if not cap.isOpened():
    print("Error: webcam")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Detect faces
    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces_rect:
        rect_roi = cv.resize(gray[y:y+h, x:x+w], (200, 200))  # Resize to match training images

        label, confidence = face_recognizer.predict(rect_roi)

        if confidence < 100:  # Threshold confidence
            name = people[label]
        else:
            name = "Unknown"

        print(f'Person Detected: {name} with confidence: {confidence:.2f}')

        # rectangle and label
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv.putText(frame, f"{name} ({int(confidence)})", (x, y-10), cv.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 2)

    cv.imshow("Live Face Recognition", frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()