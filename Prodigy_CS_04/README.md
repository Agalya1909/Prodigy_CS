# Simple Keylogger

## Introduction

The Simple Keylogger is a Python script designed to capture keystrokes from the user's keyboard and store them in a log file. It utilizes the pynput library to monitor keyboard events and record the keys pressed by the user.

## Description

This script acts as a basic keylogger, capturing keystrokes as they are typed and storing them in a text file named "keylog.txt". Each keystroke is recorded and appended to the log file in real-time. The keylogger runs in the background and continues to capture keystrokes until the user presses the 'esc' key to terminate the program.

## Libraries Used

- pynput: The pynput library is used to monitor keyboard events and capture keystrokes.

## Usage

1. Run the script in a Python environment.
2. The keylogger will start monitoring keyboard events silently in the background.
3. Type any text or press keys on the keyboard.
4. The keystrokes will be logged and stored in the "keylog.txt" file.
5. Press the 'esc' key to stop the keylogger and terminate the program.

## How it Works

1. The script initializes an empty list called `the_keys` to store the captured keystrokes.
2. A function `functionPerKey` is defined to append each pressed key to the `the_keys` list.
3. Another function `storeKeysToFile` is defined to write the captured keys to the "keylog.txt" file.
4. The `onEachKeyRelease` function checks if the 'esc' key is pressed to terminate the keylogger.
5. The script creates a Listener object with `on_press` set to `functionPerKey` and `on_release` set to `onEachKeyRelease`.
6. The Listener object starts monitoring keyboard events silently.
7. As the user types, each pressed key is appended to the `the_keys` list and stored in the "keylog.txt" file.
8. The keylogger continues to run until the 'esc' key is pressed, at which point it stops capturing keystrokes and terminates the program.

This README provides a brief overview of the Simple Keylogger script, explaining its purpose, functionality, usage instructions, and underlying techniques.
