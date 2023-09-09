from Cryptodome.Cipher import DES
from PIL import Image
import os
import sys

def generate_key():
    # Generate a random 56-bit key
    key = os.urandom(8)
    return key

def encrypt_image(image_path, key):
    # Initialize the DES cipher with the provided key and mode ECB
    cipher = DES.new(key, DES.MODE_ECB)

    # Open the image file
    image = Image.open(image_path)

    # Convert the image to RGB mode (if it's not already)
    image = image.convert("RGB")

    # Convert the image data to bytes
    image_bytes = image.tobytes()

    # Calculate the length of the image bytes
    image_length = len(image_bytes)

    # Pad the image bytes to be a multiple of 8
    if image_length % 8 != 0:
        image_bytes += b"\x00" * (8 - (image_length % 8))

    # Encrypt the image bytes
    encrypted_image_bytes = cipher.encrypt(image_bytes)

    # Create a new image from the encrypted image bytes
    encrypted_image = Image.frombytes("RGB", image.size, encrypted_image_bytes[:image_length])

    # Save the encrypted image
    encrypted_image_path = image_path.replace(".jpg", "_des_encrypted.jpg")
    encrypted_image.save(encrypted_image_path)
    print("DES Encryption complete. Encrypted image saved as:", encrypted_image_path)

    # Decrypt the encrypted image bytes
    decrypted_image_bytes = cipher.decrypt(encrypted_image_bytes)

    # Create a new image from the decrypted image bytes
    decrypted_image = Image.frombytes("RGB", image.size, decrypted_image_bytes[:image_length])

    # Save the decrypted image
    decrypted_image_path = image_path.replace(".jpg", "_des_decrypted.jpg")
    decrypted_image.save(decrypted_image_path)
    print("DES Decryption complete. Decrypted image saved as:", decrypted_image_path)

if __name__ == "__main__":
    # Generate a random key
    key = generate_key()

    # Receive the image path from the command-line argument
    image_path = sys.argv[1]

    # Encrypt and decrypt the image
    encrypt_image(image_path, key)

