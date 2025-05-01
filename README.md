Image Processing &  Webcam Color Detection using OpenCV

This project has two main parts:

1. Image Processing** – Load, convert to grayscale, blur, and detect edges in images.
2. Webcam Color Detection** – Use your webcam to detect the closest color when you click on the video.
Features
Image Processing
- Load images from a folder
- Convert images to grayscale (black & white)
- Apply Gaussian blur
- Detect edges using the Canny algorithm
- Save all processed images in an output folder
 Webcam Color Detection
- Open live webcam feed
- Detect color at the position where you click
- Match it with the closest color name from a CSV file
- Show the color name and BGR values on the video
Folder Structure
Image-Processing-and-Color-Detection/
├── src/
│   ├── image_processing.py         
│   └── webcam_color_detection.py    
├── requirements.txt               
├── Dataset/
│   ├── Images/              
│   └── csv/
│       └── colors.csv               
├── outputs/                        
└── README.md 
Setup
1. Clone the Repository
To get started, clone this repository to your local machine using the following command:
git clone https://github.com/yourusername/Image-Processing-and-Color-Detection.git
2. Install Dependencies
Navigate to the project folder and install the required libraries using pip:
cd Image-Processing-and-Color-Detection
pip install -r requirements.txt
3. Prepare the Dataset
Place your input images in the Dataset/Images folder. This folder will contain the original images that will be processed.
Ensure that you have the colors.csv file in Dataset/csv/, which contains color names and their corresponding RGB values.
Usage
1. Image Processing
To process all the images, simply run the following command:
python src/image_processing.py
This script will:
Load images from Dataset/Images/
Convert them to grayscale, apply Gaussian blur, and perform Canny edge detection
Save the processed images in outputs/
2. Webcam Color Detection
To start detecting colors in real-time from your webcam feed, run:
python src/webcam_color_detection.py
This script will:
Open the webcam feed
Allow you to click on any part of the feed to detect the color at that pixel
Display the closest matching color name and RGB values

outputs
Image Processing

![image](https://github.com/user-attachments/assets/9a0b8b16-3253-4b78-b88a-0cd4c24b591d)

Webcam

![image](https://github.com/user-attachments/assets/7038d5f0-b7e2-412d-a819-2ffc66707f10)
