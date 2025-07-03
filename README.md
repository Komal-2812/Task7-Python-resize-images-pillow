# Task7-Python-resize-images-pillow
🖼️ Image Resizer Tool

## ✅ Objective
Resize and convert all images in a folder using Python and Pillow.

## 🛠 Tools
- Python
- Pillow (PIL)
- os module

##  📁 Folder Structure

task 7/
├── input_images/  Put original images here
├── output_images/  Resized and converted images saved here
├── app.py  Python script
└── README.md

##  🚀 How to Run
1. Install Pillow: `pip install pillow`
2. Place your images inside `input_images/`
3. Run script: `python app.py`

## 🎯 Output
All images resized to 800x800 and converted to PNG.

## 🧠 1. What is Pillow?
Pillow is a Python imaging library used for opening, manipulating, and saving images.
It’s the modern fork of the original PIL (Python Imaging Library) and supports formats like PNG, JPEG, BMP, and more.

## 📂 2. How do you open and save images?
Using Pillow:

from PIL import Image

img = Image.open("input.jpg")      # Open image

img.save("output.png")             # Save image

## 📏 3. What does resize() do?
resize() changes the dimensions of an image to the size you specify:

resized = img.resize((800, 800))  # Width x Height

It returns a new resized image while keeping the original unchanged.

## 📁 4. How do you loop through files in a folder? (os.listdir)
Using the os module:

import os

for file in os.listdir("input_images"):
    print(file)

This lists all files (and folders) inside input_images.
