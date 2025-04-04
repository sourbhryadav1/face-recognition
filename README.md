# Self OpenCV Projects

## Overview
This repository contains five projects using OpenCV:

- **Face Recognition**: Uses the LBPH (Local Binary Patterns Histogram) algorithm to detect and recognize human faces from images, videos, and live camera feeds.
- **Simpsons Character Recognition**: Detects and recognizes characters from *The Simpsons* using DL and a Kaggle dataset.
- **Virtual Paint**: Detects specific colors from a live camera feed and tracks their movement to create virtual drawings on the screen—just like painting in the air! ✨
- **Car Plate Detection**: Detects car license plates from images and live webcam feeds using OpenCV.
- **Document Scanner**: Detects and extracts documents from live webcam feeds by performing edge detection and perspective transformation.
  
## Requirements
- Python 3.x
- OpenCV
- NumPy

## Install Dependencies
```bash
pip install opencv-python opencv-contrib-python numpy
```

## 📂 Project Structure
```
face-recognition/
    face_train.py
    face_test.py
    face_live.py
    haar_face.xml

simpsons-recognition/
    simpsons.ipynb

virtual-paint/
    color-picker.py
    main.py

color-plate-detect/
    photos.py
    webcam.py
    haar_russian_plates.xml

doc-scanner/
    main.py
```

## 👨‍💻 Author
Sourabh
