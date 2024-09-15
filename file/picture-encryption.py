from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random
import os

# Function to generate RSA key pair
def generate_key_pair():
    random_generator = Random.new().read
    key = RSA.generate(2048, random_generator)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

# Function to encrypt data using RSA public key
def encrypt_data(data, public_key):
    cipher_rsa = PKCS1_OAEP.new(RSA.import_key(public_key))
    ciphertext = cipher_rsa.encrypt(data)
    return ciphertext

# Function to decrypt data using RSA private key
def decrypt_data(ciphertext, private_key):
    cipher_rsa = PKCS1_OAEP.new(RSA.import_key(private_key))
    plaintext = cipher_rsa.decrypt(ciphertext)
    return plaintext

# Function to read data from file
def read_data(file_path):
    with open(file_path, 'rb') as file:
        return file.read()

# Function to write data to file
def write_data(data, file_path):
    with open(file_path, 'wb') as file:
        file.write(data)

# Main function
if __name__ == "__main__":
    print("Welcome to Image Encryption/Decryption App")
    print("1. Encrypt Image")
    print("2. Decrypt Image")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        # Generate RSA key pair
        private_key, public_key = generate_key_pair()

        # Save keys to files
        with open('private_key.pem', 'wb') as file:
            file.write(private_key)
        with open('public_key.pem', 'wb') as file:
            file.write(public_key)

        # Encrypt image
        image_path = input("Enter the path of the image file to encrypt: ")
        image_data = read_data(image_path)
        encrypted_image_data = encrypt_data(image_data, public_key)
        write_data(encrypted_image_data, 'encrypted_image.jpg')
        print("Image encrypted successfully.")

    elif choice == '2':
        # Load RSA private key
        private_key_path = input("Enter the path of the private key file: ")
        private_key = read_data(private_key_path)

        # Decrypt image
        encrypted_image_path = input("Enter the path of the encrypted image file: ")
        encrypted_image_data = read_data(encrypted_image_path)
        decrypted_image_data = decrypt_data(encrypted_image_data, private_key)
        write_data(decrypted_image_data, 'decrypted_image.jpg')
        print("Image decrypted successfully.")

    else:
        print("Invalid choice. Please enter 1 or 2.")