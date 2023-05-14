from cryptography.fernet import Fernet, InvalidToken
import sys

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    with open("key.key", "rb") as key_file:
        key = key_file.read()
    return key

def view():
    try:
        with open("passwords.txt", "r") as f:
            for line in f.readlines():
                data = line.rstrip()
                user, passw = data.split("|")
                try:
                    decrypted_password = fer.decrypt(passw.encode()).decode()
                    print("User:", user, "| Password: ", decrypted_password)
                except InvalidToken:
                    print("Invalid password format. Skipping the entry.")
    except FileNotFoundError:
        print("Password file not found.")

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    encrypted_password = fer.encrypt(pwd.encode()).decode()
    with open("passwords.txt", "a") as f:
        f.write(name + "|" + encrypted_password + "\n")

write_key()
key = load_key()
fer = Fernet(key)


while True:
    mode = input("Would you like to add a new password or view existing ones? (view, add), press q to quit? ").lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue