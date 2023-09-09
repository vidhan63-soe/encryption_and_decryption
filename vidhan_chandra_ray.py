# -*- coding: utf-8 -*-
"""vidhan_chandra_ray.ipynb


Original file is located at
    https://colab.research.google.com/drive/1ZmB1hxUB5bII8gPjm__vbkfJbttUV6wc
"""

# Vidhan Chandra Ray 
# 20/11/EC/020
# Visual Cryptography Coding (base PYTHON)

! pip install pycryptodome

from Crypto.Cipher import DES
from PIL import Image
import os
import secrets

# Provide the path to the image you want to encrypt
image_path = "/content/target.jpg"

# Extract the directory path and the image file name
image_dir, image_filename = os.path.split(image_path)

# Generate the paths for encrypted image, decrypted image, and final image
encrypted_image_path = os.path.join(image_dir, "encrypted_" + image_filename)
decrypted_image_path = os.path.join(image_dir, "decrypted_" + image_filename)
final_image_path = os.path.join(image_dir, "final_" + image_filename)

# Generate a random 56-bit key for DES encryption
key = secrets.token_bytes(8)

# Initialize the DES cipher with the generated key and mode ECB
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
encrypted_image.save(encrypted_image_path)
print("Encryption complete. Encrypted image saved as:", encrypted_image_path)

# Decrypt the image bytes
decrypted_image_bytes = cipher.decrypt(encrypted_image_bytes)

# Create a new image from the decrypted image bytes
decrypted_image = Image.frombytes("RGB", image.size, decrypted_image_bytes[:image_length])

# Save the decrypted image
decrypted_image.save(decrypted_image_path)
print("Decryption complete. Decrypted image saved as:", decrypted_image_path)

# Create a new image from the original image bytes
final_image = Image.frombytes("RGB", image.size, image_bytes[:image_length])

# Save the final image (original image)
final_image.save(final_image_path)
print("Final image (original) saved as:", final_image_path)

from Crypto.Cipher import DES3

# Provide the path to the image you want to encrypt
image_path = "/content/target.jpg"

# Extract the directory path and the image file name
image_dir, image_filename = os.path.split(image_path)

# Generate the paths for encrypted image, decrypted image, and final image
encrypted_image_path = os.path.join(image_dir, "encrypted_3des_" + image_filename)
decrypted_image_path = os.path.join(image_dir, "decrypted_3des_" + image_filename)
final_image_path = os.path.join(image_dir, "final_3des_" + image_filename)

# Generate a random 168-bit key (24 bytes)
key = os.urandom(24)

# Initialize the Triple DES cipher with the generated key
cipher = DES3.new(key, DES3.MODE_ECB)



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
encrypted_image.save(encrypted_image_path)
print("Encryption complete. Encrypted image saved as:", encrypted_image_path)

# Decrypt the image bytes
decrypted_image_bytes = cipher.decrypt(encrypted_image_bytes)

# Create a new image from the decrypted image bytes
decrypted_image = Image.frombytes("RGB", image.size, decrypted_image_bytes[:image_length])

# Save the decrypted image
decrypted_image.save(decrypted_image_path)
print("Decryption complete. Decrypted image saved as:", decrypted_image_path)

# Create a new image from the original image bytes
final_image = Image.frombytes("RGB", image.size, image_bytes[:image_length])

# Save the final image (original image)
final_image.save(final_image_path)
print("Final image (original) saved as:", final_image_path)

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


# Image path
image_path = "/content/target.jpg"

# AES key
key = get_random_bytes(32)  # 256-bit key

# Encrypt the image
cipher = AES.new(key, AES.MODE_ECB)
encrypted_data = b""

with open(image_path, "rb") as f:
    while True:
        chunk = f.read(16)  # Read 16 bytes (128 bits) at a time
        if len(chunk) == 0:
            break
        elif len(chunk) % 16 != 0:
            chunk = pad(chunk, 16)  # Pad the last chunk if needed
        encrypted_chunk = cipher.encrypt(chunk)
        encrypted_data += encrypted_chunk

# Save the encrypted image
encrypted_image_path = "/content/encrypted_image_AES.jpg"
with open(encrypted_image_path, "wb") as f:
    f.write(encrypted_data)

print("Encryption complete. Encrypted image saved as:", encrypted_image_path)

# Decrypt the image
cipher = AES.new(key, AES.MODE_ECB)
decrypted_data = b""

with open(encrypted_image_path, "rb") as f:
    while True:
        chunk = f.read(16)  # Read 16 bytes (128 bits) at a time
        if len(chunk) == 0:
            break
        decrypted_chunk = cipher.decrypt(chunk)
        decrypted_data += decrypted_chunk

# Remove padding from the last chunk
decrypted_data = unpad(decrypted_data, 16)

# Save the decrypted image
decrypted_image_path = "/content/decrypted_image_AES.jpg"
with open(decrypted_image_path, "wb") as f:
    f.write(decrypted_data)

print("Decryption complete. Decrypted image saved as:", decrypted_image_path)

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


# Image path
image_path = "/content/target.jpg"

# Generate RSA key pair
key = RSA.generate(2048)  # 256-bit key

# Encrypt the image
cipher_rsa = PKCS1_OAEP.new(key.publickey())
encrypted_data = b""

with open(image_path, "rb") as f:
    while True:
        chunk = f.read(128)  # Read 128 bytes (1024 bits) at a time
        if len(chunk) == 0:
            break
        encrypted_chunk = cipher_rsa.encrypt(chunk)
        encrypted_data += encrypted_chunk

# Save the encrypted image
encrypted_image_path = "/content/encrypted_image_RSA.jpg"
with open(encrypted_image_path, "wb") as f:
    f.write(encrypted_data)

print("Encryption complete. Encrypted image saved as:", encrypted_image_path)

# Decrypt the image
cipher_rsa = PKCS1_OAEP.new(key)
decrypted_data = b""

with open(encrypted_image_path, "rb") as f:
    while True:
        chunk = f.read(256)  # Read 256 bytes (2048 bits) at a time
        if len(chunk) == 0:
            break
        decrypted_chunk = cipher_rsa.decrypt(chunk)
        decrypted_data += decrypted_chunk

# Save the decrypted image
decrypted_image_path = "/content/decrypted_image_RSA.jpg"
with open(decrypted_image_path, "wb") as f:
    f.write(decrypted_data)

print("Decryption complete. Decrypted image saved as:", decrypted_image_path)
