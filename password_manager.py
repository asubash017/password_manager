from cryptography.fernet import Fernet
from hashlib import sha256
import base64
import os


master_pwd = input("Enter your master password: ")


key = base64.urlsafe_b64encode(sha256(master_pwd.encode()).digest())
fer = Fernet(key)  # Create Fernet object for encryption/decryption


def add():
    """Add a new password"""
    name = input("Account Name: ")
    pwd = input("Password: ")
    encrypted_pwd = fer.encrypt(pwd.encode()).decode()  

    with open("passwords.txt", "a") as f:
        f.write(f"{name}|{encrypted_pwd}\n")
    print(f"Password for {name} saved successfully!\n")

def view():
    """View stored passwords"""
    if not os.path.exists("passwords.txt"):
        print("No passwords stored yet.\n")
        return

    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            try:
                user, encrypted_pwd = data.split("|")
                decrypted_pwd = fer.decrypt(encrypted_pwd.encode()).decode() 
                print(f"User: {user} | Password: {decrypted_pwd}")
            except Exception:
                print(f"Error reading line: {data}")

    print()  


while True:
    mode = input("Would you like to add a new password or view existing ones (add, view), or quit (q)? ").lower()
    if mode == "q":
        print("Goodbye!")
        break
    elif mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("Invalid option. Try again.\n")
    
    
