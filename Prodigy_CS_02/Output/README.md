# Pixel Manipulation for Image Encryption




## Introduction

Pixel Manipulation for Image Encryption is a Python script that implements a simple image encryption technique using pixel manipulation. This script allows users to encrypt and decrypt images using a secret key generated during the encryption process.




## Description

The script employs numpy for numerical computations and the PIL (Python Imaging Library) module for image processing tasks. It encrypts the input image by shuffling the pixel values using a random permutation. The permutation used during encryption is stored as part of the secret key. The script provides options for displaying the original image, encrypted image, and decrypted image using the generated secret key.




## Libraries or Language Used

Python: The script is written in Python, a high-level programming language known for its versatility and ease of use.
numpy: The numpy library is used for numerical computations and array manipulation, which are essential for pixel shuffling.
PIL (Python Imaging Library): The PIL module is used for opening, manipulating, and saving images in various formats.




## Usage

1. Run the script in a Python environment.
2. Enter the path to the image file when prompted.
3. The script will encrypt the image and generate a secret key.
4. Choose an option to display the original image, encrypted image, or decrypted image using the secret key.
5. Optionally, enter the secret key to decrypt the image.




## Example

### Code

```python
Enter the image path: example_image.jpg

Choose an option to display the image:
1: Original Image
2: Encrypted Image
3: Decrypted Image
4: Terminate
Enter your choice (1, 2, 3, or 4): 1
```




## How it Works

1. The script opens the input image and converts it to a numpy array.
2. It flattens the pixel values of the image and generates a random permutation of the indices.
3. The pixel values are shuffled using the permutation to encrypt the image.
4. During encryption, a secret key is generated and saved to a file.
5. The script provides options to display the original, encrypted, and decrypted images using the generated secret key.

This README provides a comprehensive overview of the Pixel Manipulation for Image Encryption script, explaining its purpose, functionality, usage instructions, example, and underlying techniques.




