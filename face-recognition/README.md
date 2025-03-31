# Face Recognition using OpenCV

## Overview
This project implements face recognition using OpenCV's LBPH (Local Binary Patterns Histogram) algorithm. It allows you to train a model on a set of labeled images and then recognize faces in images, videos, or live camera feeds.

## Features
- Train a model on labeled images.
- Detect and recognize faces in test images.
- Live face recognition using a webcam.

## Requirements
- Python 3.x
- OpenCV
- NumPy

### Install Dependencies
```bash
pip install opencv-python opencv-contrib-python numpy
```

## Setup and Usage

### 1. Prepare the Dataset
Create a folder structure like this:
```
train/
    person1/
        img1.jpg
        img2.jpg
    person2/
        img1.jpg
        img2.jpg
    person3/
        img1.jpg
        img2.jpg
```

### 2. Train the Model
Run the training script to train and save the face recognition model:
```bash
python face_train.py
```
This will generate `face_trained.yml`, `features.npy`, and `labels.npy`.

### 3. Test on an Image
Run the following script to test face recognition on a static image:
```bash
python face_test.py
```

### 4. Live Face Recognition
To use live webcam detection, run:
```bash
python face_live.py
```

## File Descriptions
- **face_train.py** - Trains the face recognition model using labeled images.
- **face_test.py** - Tests the trained model on a single image.
- **face_live.py** - Performs real-time face recognition using a webcam.
- **haar_face.xml** - Pre-trained Haar cascade classifier for face detection.
- **face_trained.yml** - Saved face recognition model.
- **features.npy & labels.npy** - NumPy arrays containing training data.

## Future Improvements
- Add support for more advanced deep learning models (e.g., OpenCV DNN or FaceNet).
- Improve accuracy with better preprocessing techniques.
- Implement real-time recognition on mobile devices.

## Author
Sourabh
