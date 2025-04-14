# Handwritten Digit Recognition using KNN 🎯🧠

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

This project is a simple and interactive handwritten digit recognition system built using:

- Python 🐍
- Scikit-Learn
- OpenCV
- Tkinter
- Pillow
- Joblib

It uses the `load_digits` dataset from `sklearn` and a K-Nearest Neighbors (KNN) classifier to recognize hand-drawn digits through a custom GUI.

---

## 💡 Features

- 🎨 Draw any digit (0-9) directly on the canvas.
- 🧠 Predict the digit using a pre-trained KNN model.
- 💾 Save your drawings as images.
- ♻️ Clear and redraw easily.
- 🚀 Fast and simple — great for learning machine learning fundamentals!

---

## 🚀 How It Works

1. The model is trained on `sklearn`’s `load_digits` dataset.
2. The drawn digit is preprocessed using OpenCV:
   - Contour detection isolates the digit.
   - Image is resized to 8x8 pixels.
   - Pixel values are scaled to match the training data.
3. The pre-trained KNN model predicts the digit.
4. The result is displayed on the GUI.

---

## 🏗️ How to Run


1. Clone this repository:
```bash
git clone https://github.com/Kalana2/HandWritten-Digit-Recognition.git
cd handwritten-digit-knn
```
2. Install dependencies:
```bash
pip install numpy scikit-learn matplotlib opencv-python pillow joblib
```
3. Run the GUI:
```bash
python digit_recognition.py
```
