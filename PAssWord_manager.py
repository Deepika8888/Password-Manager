import tkinter as tk 
from tkinter import messagebox
from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_pass(key, password):
    f = Fernet(key)
    return f.encrypt(password.encode()).decode()

def decrypt_pass(key, encrypted_password):
    f = Fernet(key)
    return f.decrypt(encrypted_password.encode()).decode()

passwords = {}

def add_pass():
    service = service_entry.get()
    username = username_entry.get()
    password = password_entry.get()


    if service and username and password: 
        encrypted_password = encrypt_pass(key, password)
        passwords[service] = {"username": username, "password": encrypted_password}
        messagebox.showinfo("Success", "Passwords has been added successfully.")
    else:
        messagebox.showwarning("Error", "Password not found.")

def get_pass():
    service = service_entry.get()
    if service in passwords:
        encrypted_password = passwords[service]['password']
        decrypted_password = decrypt_pass(key, encrypted_password)
        messagebox.showinfo("Password", f"Username: {passwords[service]['username']}\nPassword: {decrypted_password}")
    else:
        messagebox.showwarning("Error", "Password not found.")

key = generate_key()

#now using tkinter to make a window for my password manager

window = tk.Tk()
window.title("I am going to manage your passwords")
window.configure(bg = "Brown")

window.resizable(False, False)

center_frame = tk.Frame(window, bg="Blue")
center_frame.grid(row=0, column=0, padx=8, pady=8)

instruction_label = tk.Label(center_frame, text="Welcome to the Password manager.To add your password, fill all the area.\n To get your password, fill the account and click on get_pass", bg="pink")
instruction_label.grid(row=0, column=1, padx=15, pady=7)

service_label = tk.Label(center_frame, text="Account:", bg="Green")
service_label.grid(row=1, column=0, padx=15, pady=7)
service_entry = tk.Entry(center_frame, bg ="white")
service_entry.grid(row=1, column=1, padx=15, pady=7)

username_label = tk.Label(center_frame, text="Username:", bg="Green")
username_label.grid(row=2, column=0, padx=15, pady=7)
username_entry = tk.Entry(center_frame, bg ="white")
username_entry.grid(row=2, column=1, padx=15, pady=7)

password_label = tk.Label(center_frame, text="Password:", bg="Green")
password_label.grid(row=3, column=0, padx=15, pady=7)
password_entry = tk.Entry(center_frame, show="*")
password_entry.grid(row=3, column=1, padx=15, pady=7)

add_button = tk.Button(center_frame, text="Add Password", command=add_pass, height=1, width=10, bg="pink")
add_button.grid(row=5, column=4, padx=15, pady=7)

get_button = tk.Button(center_frame, text="Get Password", command=get_pass, height=1, width=10, bg="pink")
get_button.grid(row=6, column=4, padx=15, pady=7)

signature_label = tk.Label(center_frame, text="Deepika Chand", bg="pink")
signature_label.grid(row=7, column=1, padx=7, pady=7)


window.mainloop()