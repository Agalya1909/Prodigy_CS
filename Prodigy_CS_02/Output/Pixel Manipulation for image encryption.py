import numpy as np
from PIL import Image
import random
import matplotlib.pyplot as plt
import os
import string

def encrypt_image(image_path):
    # Open the image
    image = Image.open(image_path)
    # Convert the image to a numpy array
    data = np.array(image)
    # Get the shape of the image
    original_shape = data.shape
    # Flatten the image data
    flat_data = data.flatten()
    # Generate a random permutation of the indices
    permutation = np.random.permutation(flat_data.size)
    # Shuffle the flat data using the permutation
    encrypted_flat_data = flat_data[permutation]
    # Reshape the encrypted data back to the original shape
    encrypted_data = encrypted_flat_data.reshape(original_shape)
    # Convert the numpy array back to an image
    encrypted_image = Image.fromarray(encrypted_data.astype('uint8'))
    
    return encrypted_image, permutation

def decrypt_image(encrypted_image, permutation):
    # Convert the encrypted image to a numpy array
    encrypted_data = np.array(encrypted_image)
    # Get the shape of the encrypted image
    original_shape = encrypted_data.shape
    # Flatten the encrypted data
    flat_encrypted_data = encrypted_data.flatten()
    # Create an array to hold the decrypted data
    decrypted_flat_data = np.zeros_like(flat_encrypted_data)
    # Unshuffle the flat encrypted data using the permutation
    decrypted_flat_data[permutation] = flat_encrypted_data
    # Reshape the decrypted data back to the original shape
    decrypted_data = decrypted_flat_data.reshape(original_shape)
    # Convert the numpy array back to an image
    decrypted_image = Image.fromarray(decrypted_data.astype('uint8'))
    
    return decrypted_image

def generate_secret_key():
    # Generate a random secret key with length between 3 and 6 characters
    key_length = random.randint(3, 6)
    secret_key = ''.join(random.choices(string.ascii_letters + string.digits, k=key_length))
    return secret_key

def save_secret_key(secret_key, key_path):
    with open(key_path, 'w') as f:
        f.write(secret_key)

def load_secret_key(key_path):
    with open(key_path, 'r') as f:
        return f.read().strip()

while True:
    # Get the image path from the user
    image_path = input("\nEnter the image path (or 'q' to quit): ")
    if image_path.lower() == 'q':
        print("Exiting the program.")
        break
    
    # Define the key path
    key_path = "secret_key.txt"

    # Encrypt the image
    encrypted_image, permutation = encrypt_image(image_path)

    # Generate and save the secret key
    secret_key = generate_secret_key()
    save_secret_key(secret_key, key_path)

    # Display options to the user
    while True:
        print("\nChoose an option to display the image:")
        print("1: Original Image")
        print("2: Encrypted Image")
        print("3: Decrypted Image")
        print("4: Terminate")
        option = int(input("Enter your choice (1, 2, 3, or 4): "))

        if option == 1:
            original_image = Image.open(image_path)
            plt.imshow(original_image)
            plt.title("Original Image")
            plt.axis('off')
            plt.show()
        elif option == 2:
            plt.imshow(encrypted_image)
            plt.title("Encrypted Image")
            plt.axis('off')
            plt.show()
        elif option == 3:
            entered_key = input("Enter the secret key to decrypt the image: ")
            try:
                saved_secret_key = load_secret_key(key_path)
                if entered_key == saved_secret_key:
                    decrypted_image = decrypt_image(encrypted_image, permutation)
                    plt.imshow(decrypted_image)
                    plt.title("Decrypted Image")
                    plt.axis('off')
                    plt.show()
                else:
                    print("Incorrect key! Unable to decrypt the image.")
            except Exception as e:
                print(f"Error loading the key: {e}")
        elif option == 4:
            print("Terminating the program.")
            exit()
        else:
            print("Invalid option! Please try again.")
