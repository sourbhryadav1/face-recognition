# 🎨 Virtual Paint Using OpenCV  

## 📌 Project Overview  
This is a **real-time color tracking** project using **OpenCV** in Python. It detects specific colors from a live camera feed and tracks their movement to create virtual drawings on the screen—just like painting in the air! ✨  

### 🔹 Features  
- **Tracks objects of predefined colors** 🎨  
- **Draws on the screen based on movement** ✍️  
- **Mirrors the video feed for a natural experience** 🔄  
- **Uses HSV color filtering and contour detection** 🔍  

---

## 🛠️ Technologies Used  
- **Python** 🐍  
- **OpenCV** 📷  
- **NumPy** 🔢  

---

## 🏗️ How It Works  
1. **Capture Video** 🎥 – The camera feed is accessed using OpenCV.  
2. **Color Detection** 🎨 – Predefined colors are detected in the HSV color space.  
3. **Contour Detection** 🔍 – The largest colored object is tracked.  
4. **Virtual Drawing** ✍️ – The tracked object's position is used to draw on the screen.  
5. **Mirrored Display** 🔄 – The feed is flipped for a natural interaction.  

---

## 🔧 Setup & Installation  
### 1️⃣ Clone the Repository  
```sh  
git clone https://github.com/sourbhryadav1/openCV-projects/virtual_paint.git  
cd virtual_paint
```

### 2️⃣ Install Dependencies  
```sh  
pip install opencv-python numpy  
```

### 3️⃣ Run the Project  
```sh  
python main.py
```

---

## 🎨 Using `color_picker.py` for Thresholding  
To simplify color detection, use `color_picker.py` to find the **HSV values** of any color you want to track.  

### Running `color_picker.py`:  
```sh  
python color_picker.py  
```
This script helps you determine the lower and upper HSV bounds for accurate color detection. Update the `myColors` list in `virtual_paint.py` with these values to track custom colors.

---

## 🎯 Customization  
- **🎯 Change Colors**: Modify the `myColors` list to detect different colors.  
- **🖍️ Brush Styles**: Adjust `cv.circle()` size to change brush thickness.  
- **🖥️ Resolution**: Update `frameWidth` and `frameHeight` to suit your camera.  

---

## Example Output
![output](https://github.com/sourbhryadav1/openCV-projects/blob/main/virtual_paint/results/Screenshot%202025-04-04%20121742.png)

---

## 📝 To-Do & Future Improvements  
✅ Improve gesture recognition  
✅ Add multiple color brushes  
✅ Implement an erase feature  
✅ Save drawings as images  

---

## 🤝 Contributing  
Want to improve this project? Feel free to **fork** the repo and submit a **PR**! 🚀  

---

## 📩 Contact  
📧 **Email**: sourbhr12@gmail.com
📌 **LinkedIn**: [Me](https://linkedin.com/in/sourbhryadav)  

⭐ If you found this project useful, don’t forget to **give it a star**! 🌟  

---
