from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from PIL import Image
import sys
import os

def generate_key():
    return os.urandom(24)  # 192-bit key (24 bytes),because library supports only 192 and 128 bit key.I have submitted one more file where i tried to implement 168-bit key.


def encrypt_image(image_path, key):
    cipher = Cipher(algorithms.TripleDES(key), modes.ECB(), backend=default_backend())

    image = Image.open(image_path)
    image = image.convert("RGB")
    image_bytes = image.tobytes()

    padder = padding.PKCS7(8 * 8).padder()
    padded_data = padder.update(image_bytes) + padder.finalize()

    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    encrypted_image = Image.frombytes("RGB", image.size, encrypted_data[:len(image_bytes)])

    encrypted_image_path = image_path.replace(".jpg", "_3des_encrypted.jpg")
    encrypted_image.save(encrypted_image_path)
    print("3DES Encryption complete. Encrypted image saved as:", encrypted_image_path)

# def decrypt_image(image_path, key):
#     cipher = Cipher(algorithms.TripleDES(key), modes.ECB(), backend=default_backend())

#     encrypted_image = Image.open(image_path)
#     encrypted_image = encrypted_image.convert("RGB")
#     encrypted_image_bytes = encrypted_image.tobytes()

#     decryptor = cipher.decryptor()
#     decrypted_data = decryptor.update(encrypted_image_bytes) + decryptor.finalize()

#     unpadder = padding.PKCS7(8 * 8).unpadder()
#     unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()

#     decrypted_image = Image.frombytes("RGB", encrypted_image.size, unpadded_data)

#     decrypted_image_path = image_path.replace(".jpg", "_3des_decrypted.jpg")
#     decrypted_image.save(decrypted_image_path)
#     print("3DES Decryption complete. Decrypted image saved as:", decrypted_image_path)

if __name__ == "__main__":
    # Generate a random key
    key = generate_key()

    # Receive the image path from the command-line argument
    image_path = sys.argv[1]

    # Encrypt and decrypt the image
    encrypt_image(image_path, key)
    # decrypt_image(image_path.replace(".jpg", "_3des_encrypted.jpg"), key)
