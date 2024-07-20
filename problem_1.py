import tkinter as gui
from tkinter import messagebox
import re

def validate_username(username):
    if not username:
        return "Username required"
    if len(username) > 50:
        return "Username should not exceed 50 characters."
    return None

def validate_password(password):
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Password should contain at least one special symbol."
    if not re.search(r'\d', password):
        return "Password should contain at least one number."
    if not re.search(r'[A-Z]', password):
        return "Password should contain at least one uppercase character."
    if not re.search(r'[a-z]', password):
        return "Password should contain at least one lowercase character."
    return None

def validate_email(email):
    pattern = r'^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email):
        return "Invalid email address"
    return None

def validate():
    username = entry_username.get()
    password = entry_password.get()
    email = entry_email.get()

    username_error = validate_username(username)
    password_error = validate_password(password)
    email_error = validate_email(email)

    if username_error:
        messagebox.showerror("Validation Error", username_error)
        return
    if password_error:
        messagebox.showerror("Validation Error", password_error)
        return
    if email_error:
        messagebox.showerror("Validation Error", email_error)
        return

    messagebox.showinfo("Success", "All fields looks good now")

# Creating the GUI
window = gui.Tk()
window.title("User Input Validation")

gui.Label(window, text="Username:").grid(row=0, column=0)
entry_username = gui.Entry(window)
entry_username.grid(row=0, column=1)

gui.Label(window, text="Password:").grid(row=1, column=0)
entry_password = gui.Entry(window, show="*")
entry_password.grid(row=1, column=1)

gui.Label(window, text="Email:").grid(row=2, column=0)
entry_email = gui.Entry(window)
entry_email.grid(row=2, column=1)

gui.Button(window, text="Validate", command=validate).grid(row=3, columnspan=2)

window.mainloop()
