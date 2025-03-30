import os
import cv2 as cv
import numpy as np

haar_cascade = cv.CascadeClassifier("haar_face.xml")
if haar_cascade.empty():
    print("Error loading haar_face.xml")
    exit()

people = ["me", "harshit", "ansh"]
DIR = r"C:\Pictures\Samsung Flow\train"
IMG_SIZE = (100, 100)

features = []
labels = []

def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        if not os.path.exists(path):
            print(f"not found: {path}")
            continue

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            if img_array is None:
                print(f"Failed image: {img_path}")
                continue

            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

            if len(face_rect) == 0:
                print(f"No face : {img_path}")
                continue

            for (x, y, w, h) in face_rect:
                face_roi = gray[y:y+h, x:x+w]
                resized_face = cv.resize(face_roi, IMG_SIZE)  # Resize to fixed size

                flipped = cv.flip(resized_face, 1)  # Horizontal Flip

                features.append(resized_face)
                features.append(flipped)
                labels.append(label)
                labels.append(label)

create_train()
print("Training done!")

# Convert lists to NumPy array for same shape of images..
features = np.array(features, dtype=np.uint8)
labels = np.array(labels, dtype=np.int32)

#
# print(f"Features dtype: {features.dtype}")  # Should be uint8
# print(f"Labels dtype: {labels.dtype}")  # Should be int32
# print(f"Features shape: {features.shape}")  # Should be (num_samples, 100, 100)
# print(f"Labels shape: {labels.shape}")  # Should be (num_samples)

# Initialize Recognizer
face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Train recognizer
face_recognizer.train(features, labels)

# Save trained model
face_recognizer.save("face_trained.yml")
np.save("features.npy", features)
np.save("labels.npy", labels)

print("Model and data saved successfully!")