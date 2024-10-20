# 🚗 Number Plate Detection System

## 📚 Project Overview
The **Number Plate Detection System** is a Python-based application that detects and extracts vehicle number plates from real-time video streams using OpenCV and Tesseract OCR. It captures the number plate, processes it to extract text, and stores the information along with timestamps in an Excel file.

This project is developed under the guidance of **Dr. Gargi Shrivastav**.

## ✨ Features
- **Real-time number plate detection** using Haar Cascade classifiers.
- **OCR extraction** to recognize text from number plates.
- **Data logging**: Plate numbers along with timestamps are saved in an Excel file.
- **Error correction** for common OCR misreadings (e.g., 'O' vs '0', 'I' vs '1').
- **Graphical interface** to display the detection process in real time.

## 🛠️ Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/shivamyadavrgipt/number-plate-detection.git
    cd number-plate-detection
    ```

2. **Install Python dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up Tesseract OCR**:
   - Download and install Tesseract OCR from [here](https://github.com/tesseract-ocr/tesseract).
   - Update the Tesseract executable path in your script:
     ```python
     pytesseract.pytesseract.tesseract_cmd = r'path_to_tesseract/tesseract.exe'
     ```

4. **Download the Haar Cascade**:
   - Download the Haar Cascade for number plate detection from [here](https://github.com/opencv/opencv/tree/master/data/haarcascades).
   - Place the downloaded file in the `model/` directory.

## 🚀 Usage

1. **Run the main script**:
    ```bash
    python main.py
    ```

2. **Controls**:
   - Press **S** to save the detected number plate image and extract text.
   - Press **Q** to quit the program.

## 🖼️ Example Output
Below is an example of a detected number plate and the processed image:

*(Include a sample image of detection here)*

## 📝 Logging
- The system logs:
  - Detection of number plates.
  - OCR extraction and error correction.
  - Saving of the extracted number plate data into an Excel file.
- Logs are displayed in the terminal.

## 🛠️ Technologies Used

- **Programming Language**: Python 3.x
- **Libraries**:
  - OpenCV: Image processing and real-time display.
  - Tesseract OCR: Text extraction from images.
  - Pandas: Data logging to Excel.
  - NumPy: For numerical operations.

## 📋 Known Issues
- **OCR Accuracy**: May vary depending on the quality of the image or plate visibility.
- **Common OCR Errors**: Characters like 'O' might be recognized as '0', and 'I' as '1'. These are handled with basic corrections.

## 📄 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## 🙏 Acknowledgments
- Thanks to OpenCV for the image processing framework.
- Thanks to Tesseract OCR for enabling text extraction from images.

---

Feel free to contribute to this project and enhance the features! 😊
