from Cryptodome.Cipher import AES
from PIL import Image
import os
import sys

def generate_key():
    # Generate a random 256-bit key
    key = os.urandom(32)
    return key

def encrypt_image(image_path, key):
    # Initialize the AES cipher with the provided key and mode ECB
    cipher = AES.new(key, AES.MODE_ECB)

    # Open the image file
    image = Image.open(image_path)

    # Convert the image to RGB mode (if it's not already)
    image = image.convert("RGB")

    # Convert the image data to bytes
    image_bytes = image.tobytes()

    # Calculate the length of the image bytes
    image_length = len(image_bytes)

    # Pad the image bytes to be a multiple of 16
    if image_length % 16 != 0:
        image_bytes += b"\x00" * (16 - (image_length % 16))

    # Encrypt the image bytes
    encrypted_image_bytes = cipher.encrypt(image_bytes)

    # Create a new image from the encrypted image bytes
    encrypted_image = Image.frombytes("RGB", image.size, encrypted_image_bytes[:image_length])

    # Save the encrypted image
    encrypted_image_path = image_path.replace(".jpg", "_aes_encrypted.jpg")
    encrypted_image.save(encrypted_image_path)
    print("AES Encryption complete. Encrypted image saved as:", encrypted_image_path)

    # Decrypt the encrypted image bytes
    decrypted_image_bytes = cipher.decrypt(encrypted_image_bytes)

    # Create a new image from the decrypted image bytes
    decrypted_image = Image.frombytes("RGB", image.size, decrypted_image_bytes[:image_length])

    # Save the decrypted image
    decrypted_image_path = image_path.replace(".jpg", "_aes_decrypted.jpg")
    decrypted_image.save(decrypted_image_path)
    print("AES Decryption complete. Decrypted image saved as:", decrypted_image_path)

if __name__ == "__main__":
    # Generate a random key
    key = generate_key()

    # Receive the image path from the command-line argument
    image_path = sys.argv[1]

    # Encrypt and decrypt the image
    encrypt_image(image_path, key)
