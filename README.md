# 🚗 Number Plate Detection System

## 📚 Project Overview
The **Number Plate Detection System** uses OpenCV and Tesseract OCR to detect vehicle number plates from real-time video streams. It captures plate images, extracts the text from the plates, and stores the information in an Excel sheet with timestamps.

Project developed under the guidance of **Dr. Gargi Shrivastav**.

## ✨ Features
- Real-time number plate detection using Haar Cascade.
- OCR (Optical Character Recognition) for extracting text from plates.
- Data logging: plate number, timestamp, and date saved in an Excel file.
- Error correction for common OCR misreadings.
- Graphical display using OpenCV to show the detection in action.

## 🛠️ Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/shivamyadavrgipt/number-plate-detection.git
    cd number-plate-detection
    ```

2. Install Python dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up Tesseract OCR:
   - Download Tesseract OCR and install it from [here](https://github.com/tesseract-ocr/tesseract).
   - Update the Tesseract executable path in your script:
     ```python
     pytesseract.pytesseract.tesseract_cmd = r'path_to_tesseract/tesseract.exe'
     ```

4. Download the Haar Cascade:
   - Download the Haar Cascade for number plate detection from [here](https://github.com/opencv/opencv/tree/master/data/haarcascades) and place it in the `model/` directory.

## 🚀 Usage

1. Run the main script:
    ```bash
    python main.py
    ```

2. Controls:
   - Press **S** to save the detected number plate image and extract the text.
   - Press **Q** to exit the program.

## 📂 Project Structure

```bash
├── model/
│   └── haarcascade_russian_plate_number.xml  # Haar Cascade for plate detection
├── plates/
│   └── plates.xlsx  # Excel file for storing detected plates
├── main.py          # Main Python script
├── requirements.txt # Python dependencies
└── README.md        # Project documentation
