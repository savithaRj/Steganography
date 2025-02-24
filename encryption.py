import cv2
import os

def encrypt_image(image_path, message, password):
    img = cv2.imread(image_path)  # Load the image
    if img is None:
        print("Error: Image not found or cannot be read.")
        return

    # Character-to-value dictionary
    d = {chr(i): i for i in range(255)}

    m, n, z = 0, 0, 0
    height, width, _ = img.shape  # Get image dimensions

    # Encoding loop
    for char in message:
        if n >= height or m >= width:
            print("Error: Message is too long for the given image size.")
            return

        img[n, m, z] = d[char]
        n += 1
        m += 1
        z = (z + 1) % 3

    # Save encrypted image in a lossless format
    encrypted_image_path = "encryptedImage.png"
    cv2.imwrite(encrypted_image_path, img)
    print(f"Message encrypted successfully! Encrypted image saved as {encrypted_image_path}")
    os.system(f"start {encrypted_image_path}")  # Open the image (Windows only)

    # Save password securely
    with open("password.txt", "w") as file:
        file.write(password)

if __name__ == "__main__":
    image_path = "mypic.jpeg"  # Update with the correct path
    message = input("Enter secret message: ")
    password = input("Enter a passcode: ")
    encrypt_image(image_path, message, password)
