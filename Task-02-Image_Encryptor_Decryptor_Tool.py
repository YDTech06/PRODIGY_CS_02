# IMPORTS
import sys
import numpy as np
import cv2
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QPushButton, QFileDialog, QVBoxLayout, QHBoxLayout,
    QWidget, QMessageBox, QFrame, QSizePolicy, QLineEdit
)
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt
from PIL import Image

# CLASS DEFINITION AND INITIALIZATION
# IMAGE ENCRYPTOR DECRYPTOR CLASS
class ImageEncryptorDecryptor(QMainWindow):
    # INITIALIZATION
    def __init__(self):
        # Initialize the ImageEncryptorDecryptor application.
        super().__init__()
        self.initUI()

    # UI INITIALIZATION
    # USER INTERFACE SETUP
    def initUI(self):
        # Set up the user interface components.
        self.setWindowTitle("Image Encryption Decryption Tool")
        self.setGeometry(100, 100, 600, 400)

        self.image_path = None
        self.image_encrypted = None
        self.key = None
        self.is_logging = False

        # Create central widget and layout.
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()

        # Create image display labels and buttons.
        self.create_image_labels(layout)
        self.create_buttons(layout)

        # Set the layout to central widget.
        central_widget.setLayout(layout)

    # IMAGE LABELS CREATION
    def create_image_labels(self, layout):
        # Create labels to display images with borders.
        self.label_original = QLabel()
        self.label_original.setFrameShape(QFrame.Box)
        self.label_original.setLineWidth(2)
        self.label_original.setAlignment(Qt.AlignCenter)
        self.label_original.setScaledContents(True)
        self.label_original.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label_original.setMinimumSize(200, 200)

        self.label_encrypted = QLabel()
        self.label_encrypted.setFrameShape(QFrame.Box)
        self.label_encrypted.setLineWidth(2)
        self.label_encrypted.setAlignment(Qt.AlignCenter)
        self.label_encrypted.setScaledContents(True)
        self.label_encrypted.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label_encrypted.setMinimumSize(200, 200)

        # Layout for original image.
        original_layout = QVBoxLayout()
        original_layout.addWidget(QLabel("Original Image"))
        original_layout.addWidget(self.label_original)

        # Layout for encrypted/decrypted image.
        encrypted_layout = QVBoxLayout()
        encrypted_layout.addWidget(QLabel("Encrypted/Decrypted Image"))
        encrypted_layout.addWidget(self.label_encrypted)

        # Combine both image layouts horizontally.
        image_layout = QHBoxLayout()
        image_layout.addLayout(original_layout, 1)
        image_layout.addLayout(encrypted_layout, 1)

        # Add image layout to main layout.
        layout.addLayout(image_layout)
        layout.addSpacing(10)  # Add spacing between image and buttons

    # BUTTONS CREATION
    def create_buttons(self, layout):
        # Create buttons for controlling image encryption, decryption, and file operations.
        button_layout = QVBoxLayout()
        button_style = "background-color: #3498db; color: white; font-weight: bold;"

        # Create a file path input box.
        self.file_path_edit = QLineEdit()
        self.file_path_edit.setPlaceholderText("Selected file path will appear here")
        self.file_path_edit.setReadOnly(True)
        self.file_path_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        # Layout for Encrypt and Decrypt buttons.
        encrypt_decrypt_layout = QHBoxLayout()

        # Encrypt Button
        btn_encrypt = QPushButton("ENCRYPT")
        btn_encrypt.setStyleSheet("background-color: green; color: white; border-radius: 5px; padding: 10px; font-weight: bold;")
        btn_encrypt.clicked.connect(self.en_fun)
        encrypt_decrypt_layout.addWidget(btn_encrypt)

        # Decrypt Button
        btn_decrypt = QPushButton("DECRYPT")
        btn_decrypt.setStyleSheet("background-color: #f44336; color: white; border-radius: 5px; padding: 10px; font-weight: bold;")
        btn_decrypt.clicked.connect(self.de_fun)
        encrypt_decrypt_layout.addWidget(btn_decrypt)

        # Add Encrypt and Decrypt buttons layout to main button layout.
        button_layout.addLayout(encrypt_decrypt_layout)

        # Layout for Choose Image, File Path, and Save Image buttons.
        choose_save_layout = QHBoxLayout()

        # Choose Image Button
        btn_choose = QPushButton("Choose Image")
        btn_choose.setStyleSheet(button_style)
        btn_choose.clicked.connect(self.open_img)
        choose_save_layout.addWidget(btn_choose)

        # Add file path input box between Choose Image and Save Image buttons.
        choose_save_layout.addWidget(self.file_path_edit)

        
        # Save Image Button
        btn_save = QPushButton("Save Image")
        btn_save.setStyleSheet(button_style)
        btn_save.clicked.connect(self.save_img)
        choose_save_layout.addWidget(btn_save)

        # Add Choose Image, File Path, and Save Image buttons layout to main button layout.
        button_layout.addLayout(choose_save_layout)

        # Layout for Reset, Download Encrypted, Download Decrypted, and Exit buttons.
        action_buttons_layout = QHBoxLayout()

        # Reset Button
        btn_reset = QPushButton("Reset")
        btn_reset.setStyleSheet(button_style)
        btn_reset.clicked.connect(self.reset)
        action_buttons_layout.addWidget(btn_reset)

        # Download Encrypt Button
        btn_download_encrypted = QPushButton("Download Encrypted")
        btn_download_encrypted.setStyleSheet(button_style)
        btn_download_encrypted.clicked.connect(self.download_encrypted)
        action_buttons_layout.addWidget(btn_download_encrypted)

        # Download Decrypt Button
        btn_download_decrypted = QPushButton("Download Decrypted")
        btn_download_decrypted.setStyleSheet(button_style)
        btn_download_decrypted.clicked.connect(self.download_decrypted)
        action_buttons_layout.addWidget(btn_download_decrypted)

        # Exit Button
        btn_exit = QPushButton("Exit")
        btn_exit.setStyleSheet(button_style)
        btn_exit.clicked.connect(self.close)
        action_buttons_layout.addWidget(btn_exit)

        # Add action buttons layout to main button layout.
        button_layout.addLayout(action_buttons_layout)

        # Add button layout to main layout.
        layout.addLayout(button_layout)

    # IMAGE DISPLAY FUNCTION
    def display_image(self, img, label):
        # Display an image on the given label.
        try:
            img = img.convert("RGB")  # Convert to RGB if needed.
            qt_image = QImage(np.array(img), img.width, img.height, img.width * 3, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(qt_image)
            label.setPixmap(pixmap)
            label.setScaledContents(True)
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Failed to display image: {str(e)}")

    # OPEN IMAGE FUNCTION
    def open_img(self):
        # Open and display an image file.
        options = QFileDialog.Options()
        self.image_path, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Image Files (*.png *.jpg *.jpeg)", options=options)
        
        if self.image_path:
            # Set the file path in the QLineEdit.
            self.file_path_edit.setText(self.image_path)
            try:
                img = Image.open(self.image_path)
                self.display_image(img, self.label_original)
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Failed to open image: {str(e)}")
        else:
            QMessageBox.warning(self, "Warning", "No image selected.")

    # ENCRYPT IMAGE FUNCTION
    def en_fun(self):
        # Encrypt the loaded image.
        if self.image_path:
            try:
                image_input = cv2.imread(self.image_path, cv2.IMREAD_GRAYSCALE)
                if image_input is not None:
                    (x1, y) = image_input.shape
                    image_input = image_input.astype(float) / 255.0
                    mu, sigma = 0, 0.1
                    self.key = np.random.normal(mu, sigma, (x1, y)) + np.finfo(float).eps
                    self.image_encrypted = image_input / self.key
                    encrypted_image = (self.image_encrypted * 255).astype(np.uint8)
                    cv2.imwrite('image_encrypted.jpg', encrypted_image, [cv2.IMWRITE_JPEG_QUALITY, 50])
                    img = Image.open('image_encrypted.jpg')
                    self.display_image(img, self.label_encrypted)
                    QMessageBox.information(self, "Encrypt Status", "Image Encrypted successfully.")
                else:
                    QMessageBox.warning(self, "Warning", "Failed to read image.")
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Failed to encrypt image: {str(e)}")
        else:
            QMessageBox.warning(self, "Warning", "No image selected.")

    # DECRYPT IMAGE FUNCTION
    def de_fun(self):
        # Decrypt the encrypted image.
        if self.image_encrypted is not None and self.key is not None:
            try:
                image_output = self.image_encrypted * self.key
                image_output = np.clip(image_output * 255.0, 0, 255)  # Ensure pixel values are valid
                decrypted_image = image_output.astype(np.uint8)
                cv2.imwrite('image_output.jpg', decrypted_image, [cv2.IMWRITE_JPEG_QUALITY, 50])
                img = Image.open('image_output.jpg')
                self.display_image(img, self.label_encrypted)
                QMessageBox.information(self, "Decrypt Status", "Image Decrypted successfully.")
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Failed to decrypt image: {str(e)}")
        else:
            QMessageBox.warning(self, "Warning", "No encrypted image to decrypt.")

    # SAVE IMAGE FUNCTION
    def save_img(self):
        # Save the displayed encrypted image to a file.
        if self.label_encrypted.pixmap():
            options = QFileDialog.Options()
            file_path, _ = QFileDialog.getSaveFileName(self, "Save Image File", "", "Image Files (*.png *.jpg *.jpeg)", options=options)
            if file_path:
                try:
                    pixmap = self.label_encrypted.pixmap()
                    image = pixmap.toImage()
                    image.save(file_path)
                    QMessageBox.information(self, "Save Status", "Image saved successfully.")
                except Exception as e:
                    QMessageBox.warning(self, "Error", f"Failed to save image: {str(e)}")
            else:
                QMessageBox.warning(self, "Warning", "No file path specified.")
        else:
            QMessageBox.warning(self, "Warning", "No image to save.")

    # RESET IMAGE FUNCTION
    def reset(self):
        # Reset the application state.
        self.image_path = None
        self.image_encrypted = None
        self.key = None
        self.label_original.clear()
        self.label_encrypted.clear()
        self.file_path_edit.clear()

    # DOWNLOAD ENCRYPTED IMAGE
    def download_encrypted(self):
        # Download the encrypted image file.
        if self.image_encrypted is not None:
            try:
                options = QFileDialog.Options()
                file_path, _ = QFileDialog.getSaveFileName(self, "Save Encrypted Image", "", "Image Files (*.png *.jpg *.jpeg)", options=options)
                if file_path:
                    cv2.imwrite(file_path, (self.image_encrypted * 255).astype(np.uint8))
                    QMessageBox.information(self, "Download Status", "Encrypted image downloaded successfully.")
                else:
                    QMessageBox.warning(self, "Warning", "No file path specified.")
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Failed to download encrypted image: {str(e)}")
        else:
            QMessageBox.warning(self, "Warning", "No encrypted image to download.")

    # DOWNLOAD DECRYPTED IMAGE
    def download_decrypted(self):
        # Download the decrypted image file.
        if self.label_encrypted.pixmap():
            try:
                options = QFileDialog.Options()
                file_path, _ = QFileDialog.getSaveFileName(self, "Save Decrypted Image", "", "Image Files (*.png *.jpg *.jpeg)", options=options)
                if file_path:
                    pixmap = self.label_encrypted.pixmap()
                    image = pixmap.toImage()
                    image.save(file_path)
                    QMessageBox.information(self, "Download Status", "Decrypted image downloaded successfully.")
                else:
                    QMessageBox.warning(self, "Warning", "No file path specified.")
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Failed to download decrypted image: {str(e)}")
        else:
            QMessageBox.warning(self, "Warning", "No decrypted image to download.")

    # APPLICATION EXIT 
    # CLOSE EVENT HANDLING
    def closeEvent(self, event):
    
        # Prompt the user to confirm quitting the application.
        if self.is_logging:
            self.stop_logging()  # Ensure logging stops before quitting
        reply = QMessageBox.question(self, 'Quit', "Do you want to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

# MAIN FUNCTION
def main():
    # Initialize the application and the main window.
    app = QApplication(sys.argv)
    main_window = ImageEncryptorDecryptor()
    main_window.show()
    sys.exit(app.exec_())

# ENTRY POINT
if __name__ == "__main__":
    main()
