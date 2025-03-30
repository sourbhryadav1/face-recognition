import os
import numpy as np
import cv2 as cv

# Load Haar Cascade
haar_cascade = cv.CascadeClassifier("haar_face.xml")
if haar_cascade.empty():
    print("Error loading haar_face.xml. Ensure it exists in the directory.")
    exit()

people = ["me", "harshit", "ansh"]

# Load trained model
if not os.path.exists("face_trained.yml"):
    print("Error: Trained model file not found.")
    exit()

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read("face_trained.yml")

# Load test image
img_path = r"C:\Pictures\Samsung Flow\train\ansh\IMG-20250330-WA0013.jpg"
img = cv.imread(img_path)

if img is None:
    print(f"Error: Image not found at {img_path}")
    exit()

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Detect face
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

for (x, y, w, h) in faces_rect:
    rect_roi = cv.resize(gray[y:y+h, x:x+w], (200, 200))  # Resize to match training images

    label, confidence = face_recognizer.predict(rect_roi)
    print(f'Person Detected: {people[label]} with confidence: {confidence:.2f}')

    # Draw rectangle and label on image
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv.putText(img, f"{people[label]} ({int(confidence)})", (x, y-10), cv.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 2)

resized_img = cv.resize(img, (600, 800), interpolation=cv.INTER_AREA)  # Resize to 600x800
cv.imshow("Detected Person", resized_img)
# cv.imshow("Detected Person", img)
cv.waitKey(0)
cv.destroyAllWindows()