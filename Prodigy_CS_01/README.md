# Implementation of Caesar Cipher

## Introduction
The Caesar Cipher is a classic encryption technique used to encode messages by shifting each letter in the plaintext by a fixed number of positions down or up the alphabet. It is one of the simplest and earliest known encryption methods.

## Description
This Python script implements the Caesar Cipher encryption algorithm. It allows users to input a plaintext message and a shift value, and then generates the corresponding ciphertext by applying the Caesar Cipher algorithm.

## Libraries or Language Used
- **Python**: The script is written in Python, a high-level programming language known for its simplicity and readability.
- **Standard Libraries**: The script utilizes standard Python libraries such as `input`, `ord`, and `chr` for input/output and character manipulation.

## Usage

1. Run the script in a Python environment.
2. Enter the plaintext to be encrypted when prompted.
3. Enter the shift value (an integer) to specify the encryption pattern.
4. The script will output the encrypted ciphertext.

## Example

```plaintext
Enter the plaintext: Hello World
Enter the shift value: 3
Plain Text is : Hello World
Shift pattern is : 3
Cipher Text is : Khoor Zruog
```

## How it works

1. The script accepts a plaintext input from the user.
2. It then accepts a shift value, which determines how many positions each letter in the plaintext will be shifted.
3. The `encrypt_text` function iterates over each character in the plaintext.
4. For each character, it checks if it's a space, uppercase letter, or lowercase letter.
5. Based on the type of character, it applies the Caesar Cipher encryption by shifting the character's ASCII value by the specified shift value.
6. The encrypted ciphertext is then returned and displayed to the user.



