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

## 👨‍💻 Author
Sourabh

