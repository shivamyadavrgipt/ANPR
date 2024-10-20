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

##🖼️ Example Output
Below is an example of a detected number plate and the processed image:

(Include a sample image here)

##📝 Logging
The system uses the logging library to track important events:

Detection of number plates and saving of images.
OCR processing and corrections.
Saving the plate data to an Excel file.
Logs are displayed in the terminal.
##🛠️ Technologies Used
Programming Language: Python 3.x
Libraries:
OpenCV
Tesseract OCR
Pandas
NumPy
##📋 Known Issues
OCR Accuracy: May vary depending on the quality of the image and plate visibility.
Common Errors: Characters like 'O' might be recognized as '0', 'I' as '1', etc. These are handled with basic corrections.
##📄 License
This project is licensed under the MIT License. See the LICENSE file for more details.

##🙏 Acknowledgments
Thanks to OpenCV for providing the framework for image processing.
Thanks to Tesseract OCR for making text extraction from images possible.
