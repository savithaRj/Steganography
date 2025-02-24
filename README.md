**Secure Data Hiding In Images Using Steganography!**

This project focuses on image-based steganography, where secret data is embedded within an image in a way that remains visually undetectable. It utilizes Python and OpenCV to encode and decode messages hidden within images while maintaining data integrity.

Core Functionality :
1. Message Concealment (Encoding)
   * A user can input a secret text message, which is then embedded into an image.
   * The message is converted into ASCII values and encoded diagonally across pixel data.
   * The altered image is saved in PNG format to prevent compression-related data loss.

2. Message Retrieval (Decoding)
   * The application extracts the concealed message by reading the modified image.
   * The correct passcode and message length must be provided for successful decryption.

Technical Requirements
 * Python 3.x
 * OpenCV Library

Installation
To install the necessary dependency, run:
* pip install opencv-python

This project demonstrates a practical approach to data concealment, ensuring secure message transmission without raising suspicion.







