# Password Manager

A simple and secure password manager built with Python. This program allows you to **store and view your passwords safely** using encryption with a master password.

---

## Features

- Add new passwords for any account.
- View your saved passwords (decrypted securely).
- Encrypts passwords using **Fernet symmetric encryption**.
- Master password generates the encryption key, no key file needed.
- Beginner-friendly and easy to use.

---

## How It Works

1. When you run the program, it asks for a **master password**.  
2. This master password is hashed and used to generate a **Fernet encryption key**.  
3. You can **add** passwords for your accounts, which are encrypted and stored in `passwords.txt`.  
4. You can **view** passwords by providing the correct master password.  
5. The program ensures that your `passwords.txt` file is never uploaded to GitHub (recommended to add it to `.gitignore`).

---

## Usage

1. Run the program:

```bash
python password_manager.py
