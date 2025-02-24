import cv2

def decrypt_image(image_path, original_message_length):
    img = cv2.imread(image_path)  # Load the encrypted image
    if img is None:
        print("Error: Encrypted image not found or cannot be read.")
        return

    try:
        with open("password.txt", "r") as file:
            stored_password = file.read().strip()
    except FileNotFoundError:
        print("Error: Password file not found.")
        return

    pw = input("Enter passcode for Decryption: ")
    
    if pw != stored_password:
        print("YOU ARE NOT AUTHORIZED!")
        return

    # Value-to-character dictionary
    c = {i: chr(i) for i in range(255)}

    message = ""
    m, n, z = 0, 0, 0
    height, width, _ = img.shape  # Get image dimensions

    # Decoding loop
    for _ in range(original_message_length):  
        if n >= height or m >= width:
            print("Error: Decryption exceeded image dimensions.")
            return

        pixel_value = int(img[n, m, z])  # Ensure it's an integer
        message += c[pixel_value]
        n += 1
        m += 1
        z = (z + 1) % 3

    print("Decrypted message:", message)

if __name__ == "__main__":
    image_path = "encryptedImage.png"  # Update with the correct encrypted image path
    original_message_length = int(input("Enter the original message length reference: "))
    decrypt_image(image_path, original_message_length)
