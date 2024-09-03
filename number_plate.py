import cv2
import pytesseract
import pandas as pd
from datetime import datetime
import os
import logging

# Set up logging to output information to the console
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Path 
pytesseract.pytesseract.tesseract_cmd = r'D:\NUMBERPLATE\tesseract\tesseract.exe'

# Load the Haar Cascade for number plate detection
harcascade = r"D:\NUMBERPLATE\model\haarcascade_russian_plate_number.xml"
plate_cascade = cv2.CascadeClassifier(harcascade)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640) 
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  

min_area = 500
count = 0  # Counter for saved images

output_dir = "plates"
os.makedirs(output_dir, exist_ok=True)

# Define the path to the Excel file
excel_file_path = r'D:\NUMBERPLATE\Plates\plates.xlsx'
# Ensure the directory for the Excel file exists
os.makedirs(os.path.dirname(excel_file_path), exist_ok=True)

# Create an empty DataFrame to store plate data
plate_data = pd.DataFrame(columns=["Plate Number", "Time", "Date"])

def preprocess_image(img_roi):
    # Convert the image to grayscale
    gray = cv2.cvtColor(img_roi, cv2.COLOR_BGR2GRAY)
    # Apply Gaussian blur to the image
    blur = cv2.GaussianBlur(gray, (5, 5), 0) 
    # Apply adaptive thresholding to the image
    thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    # Dilate the image to fill gaps
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    dilate = cv2.dilate(thresh, kernel, iterations=1)
    return dilate

def correct_plate_text(plate_text):
    corrections = {'O': '0', 'I': '1', 'Q': '0', 'Z': '2', 'S': '5', 'B': '8', 'G': '6'}
    return ''.join([corrections.get(char, char) for char in plate_text])

def save_plate_data(plate_text):
    global plate_data

    now = datetime.now()

    new_data = pd.DataFrame([{
        "Date": now.strftime("%Y-%m-%d"),
        "Time": now.strftime("%H:%M:%S"),
        "Plate Number": plate_text
    }])

    plate_data = pd.concat([plate_data, new_data], ignore_index=True)
    logging.info(f"New plate data: {new_data}")

    try:
        plate_data.to_excel(excel_file_path, index=False)
        logging.info(f"Plate data saved to Excel at {excel_file_path}.")
    except Exception as e:
        logging.error(f"Failed to save plate data to Excel: {e}")

def main():
    global plate_data
    global count

    while True:
        success, img = cap.read()
        if not success:
            logging.error("Failed to capture frame. Exiting...")
            break

        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        plates = plate_cascade.detectMultiScale(img_gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in plates:
            area = w * h
            if area > min_area:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(img, "Number Plate", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)

                img_roi = img[y: y + h, x: x + w]
                processed_img = preprocess_image(img_roi)
                cv2.imshow("Processed ROI", processed_img)

        cv2.imshow("Result", img)
        key = cv2.waitKey(1) & 0xFF

        if key == ord('s'):
            if len(plates) > 0:
                count += 1
                img_filename = f"scanned_img_{count}.jpg"
                cv2.imwrite(os.path.join(output_dir, img_filename), img_roi)
                logging.info(f"Image {img_filename} saved.")

                plate_text = pytesseract.image_to_string(processed_img, config='--psm 8 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
                plate_text = ''.join(e for e in plate_text if e.isalnum())
                plate_text = correct_plate_text(plate_text)

                if plate_text:
                    logging.info(f"Detected plate: {plate_text}")
                    save_plate_data(plate_text)
                else:
                    logging.info("No plate text detected.")
            else:
                logging.info("No plate detected. Please try again.")

        if key == ord('q'):
            logging.info("Exiting program.")
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
