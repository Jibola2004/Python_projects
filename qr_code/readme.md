# 📱 QR Code Generator Script

## 📋 Description
This Python script generates a QR code from a user-provided URL. The generated QR code is saved as a `.png` file named after the platform (e.g., `youtube.png`, `facebook.png`) extracted from the URL.

## ✅ Features
- Takes a URL input from the user.
- Validates the input is not empty.
- Uses a regular expression to extract the platform name from the URL.
- Generates and saves a QR code in PNG format using the `pyqrcode` and `pypng` libraries.
- Sets a white background for the output image.

## 🧠 How It Works
1. Prompts the user for a URL.
2. Checks if the input is non-empty; raises a `ValueError` if it's invalid.
3. Uses a regex pattern to extract the platform from the URL.
4. Creates a QR code using `pyqrcode`.
5. Saves the QR code as a `.png` file with the platform name (e.g., `youtube.png`) and a white background.

