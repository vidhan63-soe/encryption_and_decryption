import subprocess
import time
import numpy as np
from PIL import Image


 image_array = convert_image_to_array(image_path)

   
    with open("target.txt", "w") as file:
        for row in image_array:
            file.write(" ".join(map(str, row)) + "\n")

def encrypt_using_des(image_path):
    des_command = ["/usr/bin/python3", "-u", "/home/vidhan/Desktop/mkai/des.py", image_path]
    subprocess.run(des_command, check=True)

def encrypt_using_3des(image_path):
    triple_des_command = ["/usr/bin/python3", "-u", "/home/vidhan/Desktop/mkai/3des.py", image_path]
    subprocess.run(triple_des_command, check=True)

def encrypt_using_aes(image_path):
    aes_command = ["/usr/bin/python3", "-u", "/home/vidhan/Desktop/mkai/aes.py", image_path]
    subprocess.run(aes_command, check=True)

def encrypt_using_rsa(image_path):
    rsa_command = ["/usr/bin/python3", "-u", "/home/vidhan/Desktop/mkai/rsa.py", image_path]
    subprocess.run(rsa_command, check=True)

def convert_image_to_array(image_path):
    image = Image.open(image_path)
    image_array = np.array(image)
    return image_array

if __name__ == "__main__":
    image_path = "/home/vidhan/Desktop/mkai/image.jpg"

    start_time = time.time()

    encrypt_using_des(image_path)

    des_execution_time = time.time() - start_time

    print("------------------")

    start_time = time.time()

    encrypt_using_3des(image_path)

    triple_des_execution_time = time.time() - start_time

    print("------------------")

    start_time = time.time()

    encrypt_using_aes(image_path)

    aes_execution_time = time.time() - start_time

    print("------------------")

    start_time = time.time()

    encrypt_using_rsa(image_path)

    rsa_execution_time = time.time() - start_time

    print("------------------")

    print("DES Encryption execution time: ", des_execution_time)
    print("3DES Encryption execution time: ", triple_des_execution_time)
    print("AES Encryption execution time: ", aes_execution_time)
    print("RSA Encryption execution time: ", rsa_execution_time)

   
   
