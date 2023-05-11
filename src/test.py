import cv2
import pytesseract

# Read image using OpenCV
img = cv2.imread('image.png')

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply OCR using Tesseract
text = pytesseract.image_to_string(gray)

# Print the extracted text
print(text)
