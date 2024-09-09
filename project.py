#Kamaaksha Rajendra Kharul
#123B1B047

import csv
import os
import getpass
from cryptography.fernet import Fernet


masterPswdFile = r"C:\Users\Dell\Desktop\ACM\masterpswd.csv"
passwordsFile = r"C:\Users\Dell\Desktop\ACM\passwords.csv"


def generate_key():
    key = Fernet.generate_key()
    with open('secret.key', 'wb') as key_file:
        key_file.write(key)
    return key


def load_key():
    if os.path.exists('secret.key'):
        with open('secret.key', 'rb') as key_file:
            return key_file.read()
    else:
        return generate_key()

key = load_key()
encrypt_loc = Fernet(key)

def check_master_pswd(user_name, pwd):
    with open(masterPswdFile, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            stored_user_name, stored_pswd = row
            if stored_user_name == user_name:
                if pwd == stored_pswd:
                    return True
                else:
                    print("Incorrect password ACCESS DENIED.")
                    return False
        print("Username not found.")
        return False

def set_pswd():
    print("Enter a password that has a length of 8 and of the format XXXX@nnn")
    pswd1 = getpass.getpass("Enter password: ")
    if len(pswd1) != 8:
        print("Password must be exactly 8 characters long.")
        return None
    lst = list(pswd1)
    flag = 0
    for i in range(4):
        if not (('A' <= lst[i] <= 'Z') or ('a' <= lst[i] <= 'z')):
            flag = 1
            break
    if lst[4] != '@':
        flag = 1
    for i in range(5, 8):
        if not lst[i].isdigit():
            flag = 1
            break
    if flag == 1:
        print("Please enter a strong password")
        return None
    else:
        return pswd1


def add_pswd():
    account_name = input("Enter account name: ")
    username = input("Enter username: ")
    password = set_pswd()
    if password != None:
        encrypted_pswd = encrypt_loc.encrypt(password.encode())
        with open(passwordsFile, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([account_name, username, encrypted_pswd.decode()])
            print("Password added successfully.")
    else:
        print("Couldn't set password")

def view_saved_pswd():
    with open(passwordsFile, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            account_name, username, encrypted_pswd = row
            decrypted_pswd = encrypt_loc.decrypt(encrypted_pswd.encode()).decode()
            print(f"Account: {account_name}, Username: {username}, Password: {decrypted_pswd}")

def delete_pswd():
    account_name = input("Enter account name to delete: ")
    username = input("Enter username: ")
    lines = []
    with open(passwordsFile, 'r') as file:
        reader = csv.reader(file)
        lines = list(reader)
    
    #Checking whether the username and account name exists
    account_found = False
    for row in lines:
        if row[0] == account_name and row[1] == username:
            account_found = True
            break
    
    if account_found:
        # Delete the account_name and username from the list
        with open(passwordsFile, 'w', newline='') as file:
            writer = csv.writer(file)
            for row in lines:
                if not (row[0] == account_name and row[1] == username):
                    writer.writerow(row)
        print("Password deleted successfully.")
    else:
        print("Account name and username not found. Deletion failed.")

def update_pswd():
    account_name = input("Enter account name to update: ")
    username = input("Enter username: ")
    #traversing the password file
    lines = []
    with open(passwordsFile, 'r') as file:
        reader = csv.reader(file)
        lines = list(reader)
    # Checking if the account_name and username exist
    account_found = False
    for row in lines:
        if row[0] == account_name and row[1] == username:
            account_found = True
            break
    if account_found:
        new_pswd = set_pswd()
        if new_pswd != None:
            encrypted_new_pswd = encrypt_loc.encrypt(new_pswd.encode())
            #Update the password
            with open(passwordsFile, 'w', newline='') as file:
                writer = csv.writer(file)
                for row in lines:
                    if row[0] == account_name and row[1] == username:
                        writer.writerow([account_name, username, encrypted_new_pswd.decode()])
                    else:
                        writer.writerow(row)
                        print("Password updated successfully.")
    else:
        print("Account name and username not found. Update failed.")


user_name = input("Enter username: ")
pwd = getpass.getpass("Enter login password: ")
if check_master_pswd(user_name, pwd):
    print("LOGIN SUCCESSFUL")
    print("Enter 1: Add password, 2: View saved passwords, 3: Delete password, 4: Update Password")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        add_pswd()
    elif ch == 2:
        view_saved_pswd()
    elif ch == 3:
        delete_pswd()
    elif ch == 4:
        update_pswd()
    else:
        print("Invalid choice")
else:
    print("LOGIN FAILED")
