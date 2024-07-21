# Password-Manager
Python project
This is a simple password manager application that I built using Python and Tkinter. The application allows you to securely store, encrypt, and retrieve passwords for different accounts.

## Project Overview

In this project, I have created a basic GUI application to manage passwords. The functionalities include:

- **Add Password**: Store a username and encrypted password for a specific account.
- **Get Password**: Retrieve and decrypt the stored password for a specific account.

## Inspiration and Learning

I created this project by watching various tutorials and reading code from other developers. This approach helped me understand different aspects of Python programming and how to build a GUI application.

## What I Learned

Through this project, I have learned and implemented several Python skills, including:

- **Tkinter**: How to create a basic graphical user interface (GUI) using Tkinter.
- **Cryptography**: How to use the `cryptography` library to encrypt and decrypt passwords securely.
- **Event Handling**: How to handle events in a GUI application, such as button clicks.
- **Data Management**: How to store and retrieve data using dictionaries in Python.

## How It Works

### Key Functions

- **generate_key()**: Generates a new encryption key using Fernet.
- **encrypt_pass(key, password)**: Encrypts the password using the provided key and returns the encrypted password.
- **decrypt_pass(key, encrypted_password)**: Decrypts the encrypted password using the provided key and returns the original password.
- **add_pass()**: Adds a new service, username, and encrypted password to the passwords dictionary.
- **get_pass()**: Retrieves and decrypts the password for a given service from the passwords dictionary.

### GUI Components

- **Labels and Entries**: Used to input and display account details (service, username, password).
- **Buttons**: Used to trigger the add and get password functions.
- **Message Boxes**: Used to show success and error messages to the user.
