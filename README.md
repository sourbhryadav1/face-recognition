# Face & Simpsons Character Recognition using OpenCV and DL

## Overview
This repository contains two projects using OpenCV for face recognition:

- **Face Recognition**: Uses the LBPH (Local Binary Patterns Histogram) algorithm to detect and recognize human faces from images, videos, and live camera feeds.
- **Simpsons Character Recognition**: Detects and recognizes characters from *The Simpsons* using DL and a Kaggle dataset.

## Features
- Train models on labeled images.
- Detect and recognize faces in static images.
- Perform real-time recognition using a webcam.

## Requirements
- Python 3.x
- OpenCV
- NumPy

## Install Dependencies
```bash
pip install opencv-python opencv-contrib-python numpy kaggle
```

## 📂 Project Structure
```
face-recognition/
    face_train.py
    face_test.py
    face_live.py
    haar_face.xml
    face_trained.yml
    features.npy
    labels.npy

simpsons-recognition/
   simpsons.ipynb
```

## 🏆 Face Recognition
### 1. Prepare the Dataset
Create a dataset folder with labeled images:
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
```bash
python face-recognition/face_train.py
```

### 3. Test on an Image
```bash
python face-recognition/face_test.py
```

### 4. Live Face Recognition
```bash
python face-recognition/face_live.py
```

## 🎭 Simpsons Character Recognition
### 1. Dataset
I have already added dataset api link from kaggel in 1st cell, you just need to run it and enjoyyyy...

### 2. Train the Model
Run the Jupyter Notebook:
```bash
jupyter notebook simpsons-recognition/simpsons_train.ipynb
```

### 3. Test on an Image
Run the appropriate cell in `simpsons_train.ipynb` to test on a static image from dataset.

## 🔧 Future Improvements
- Improve model.
- Improve dataset preprocessing for better accuracy.
- Implement mobile support for real-time recognition.

## 👨‍💻 Author
Sourabh

