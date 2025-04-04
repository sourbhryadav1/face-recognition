# Car Plate Detect using OpenCV

## Overview
This project detects CarPlates using OpenCV. It allows you to train a model on a set of labeled images and then recognize plate in images, videos, or live camera feeds.

## Features
- Train a model on labeled images.
- Detect and recognize plates in test images.
- Live plate recognition using a webcam.

## Requirements
- Python 3.x
- OpenCV
- NumPy

### Install Dependencies
```bash
pip install opencv-python opencv-contrib-python numpy
```

## Setup and Usage

### 1. Run an Test on an Image
Run the following script to test Car plate detector on a static image:
```bash
python photos.py
```

### 2. Live plate Recognition
To use live webcam detection, run:
```bash
python webcam.py
```

## File Descriptions
- **photos.py** - Detects the Car plates on static car images.
- **webcam.py** - Detects the live Car plates through webcam.
- **haar_russian_plates.xml** - Pre-trained Haar cascade classifier for car plate detection.

## Future Improvements
- Add support for more advanced deep learning models (e.g., OpenCV DNN or FaceNet).
- Improve accuracy with better preprocessing techniques.
- Implement real-time recognition on mobile devices.

## Examples of detection-
##### Input
![Input image](https://github.com/sourbhryadav1/openCV-projects/blob/main/car_plate_detect/results/image.jpg)

##### Output
![Output image](https://github.com/sourbhryadav1/openCV-projects/blob/main/car_plate_detect/results/output.jpg)


## Author
Sourabh
