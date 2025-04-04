# Document Scanner using OpenCV

## Overview
This project implements a document scanner using OpenCV. It processes images from a webcam, detects document edges, and performs a perspective transformation to get a properly aligned document view.

## Features
- Preprocess images using grayscale and adaptive thresholding.
- Detect document contours using OpenCV.
- Perform a perspective transformation to extract the document.
- Live document scanning via webcam.

## Requirements
- Python 3.x
- OpenCV
- NumPy

### Install Dependencies
```bash
pip install opencv-python numpy
```

## Setup and Usage

### 1. Run the Document Scanner
Run the following script to start the live document scanner:
```bash
python main.py
```

Press `q` to exit the webcam window.

## File Descriptions
- **main.py** - The main script for capturing and processing images to detect and extract documents.

## Working Principle
1. **Preprocessing:** Converts the image to grayscale and applies adaptive thresholding.
2. **Contour Detection:** Identifies the biggest quadrilateral in the frame (assumed to be the document).
3. **Perspective Transformation:** Warps the detected region to create a top-down view of the document.

## Example Output
![input](https://github.com/sourbhryadav1/openCV-projects/blob/main/doc_scanner/results/input.jpg)
![contours detect](https://github.com/sourbhryadav1/openCV-projects/blob/main/doc_scanner/results/contours.jpg)
![threshold](https://github.com/sourbhryadav1/openCV-projects/blob/main/doc_scanner/results/threshold.jpg)
![output](https://github.com/sourbhryadav1/openCV-projects/blob/main/doc_scanner/results/output.jpg)

## Future Improvements
- Improve accuracy using deep learning-based edge detection.
- Implement automatic document size detection.
- Add OCR functionality for text extraction.

## Author
Sourabh
