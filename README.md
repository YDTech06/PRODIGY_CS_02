# Prodigy-Infotech-CS-Tasks
# Image Encryptor Decryptor Tool

If you find this tool useful, don't forget to give it a star! ⭐

## Overview

The Image Encryptor Decryptor Tool is a user-friendly desktop application developed using Python's PyQt5. This tool allows users to encrypt and decrypt images using a simple interface. It supports functionalities for choosing images, encrypting, decrypting, saving, and downloading images.

## Features

- **Choose Image**: Select an image file to be processed.
- **Encrypt Image**: Encrypt the selected image using a simple encryption technique.
- **Decrypt Image**: Decrypt the previously encrypted image to restore the original.
- **Save Image**: Save the displayed encrypted or decrypted image to a specified file.
- **Download Encrypted Image**: Download the encrypted image file.
- **Download Decrypted Image**: Download the decrypted image file.
- **Reset**: Clear all images and reset the application state.
- **User Interface**: Clean and intuitive interface with image display areas and action buttons.

## Installation

1. **Clone or Download the Repository**:
   ```bash
   git clone https://github.com/YDTech06/PRODIGY_CS_02.git
2. **Install Dependencies**: Ensure you have the required Python libraries installed:
   ```bash
   pip install numpy opencv-python-headless PyQt5 pillow
3. Run the Script: Execute the script using Python:
   ```bash
   python image_encryptor_decryptor_tool.py

## How To Use
- **Open Image**: Click "Choose Image" to select and display an image.
- **Encrypt Image**: Click "ENCRYPT" to encrypt the displayed image. The encrypted image will be shown in the second display area.
- **Decrypt Image**: Click "DECRYPT" to decrypt the encrypted image and restore the original.
- **Save Image**: Click "Save Image" to save the displayed encrypted or decrypted image to a file.
- **Download Encrypted**: Click "Download Encrypted" to save the encrypted image to a file.
- **Download Decrypted**: Click "Download Decrypted" to save the decrypted image to a file.
- **Reset**: Click "Reset" to clear the images and reset the application state.
- **Exit**: Click "Exit" to close the application. You will be prompted to confirm quitting.

## Notes
1. Ensure that you have a valid image file selected before attempting encryption or decryption.
2. The encryption method used here is a basic form and is not suitable for high-security requirements.
3. The tool is intended for educational purposes and simple image processing tasks.
