readme_content = """
# Number Plate Detection System

[![GitHub License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-blue)
![Python](https://img.shields.io/badge/Python-3.x-blue)

## Project Overview

This project is a **Number Plate Detection System** developed using OpenCV and Tesseract OCR. The system captures images from a live video feed, detects vehicle number plates, and extracts text using Optical Character Recognition (OCR). The extracted data is saved to an Excel file, along with a timestamp for each detected plate.

The project was developed under the guidance of **Dr. Gargi Shrivastav**.

## Features

- Real-time video capture and number plate detection using Haar Cascades.
- Image preprocessing techniques for better OCR accuracy.
- Text extraction from the number plates using Tesseract OCR.
- Automatic correction of common OCR errors (e.g., converting 'O' to '0', 'S' to '5').
- Storing the plate number and timestamp in an Excel file for future reference.
- Easy-to-use GUI interface via OpenCV for displaying the results.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/shivamyadavrgipt/number-plate-detection.git
   cd number-plate-detection
