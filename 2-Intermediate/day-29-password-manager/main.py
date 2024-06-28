from tkinter import messagebox, root
from tkinter import *
import pyperclip
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    password_chars = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()1234567890")
    for _ in range(16):
        password_entry.insert(END, random.choice(password_chars))
    pyperclip.copy(password_entry.get())
# ---------------------------- SAVE PASSWORD ------------------------------- #
def dialog_box():
    if len(website_entry.get()) == 0 or len(email_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website_entry.get(), message=f"These are the details entered: Website: {website_entry.get()}\nEmail: {email_entry.get()}\nPassword: {password_entry.get()}\nIs it ok to save?")
        if is_ok:
            save_data()

def save_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    with open("passwords.txt", "a") as file:
        file.write(f"{website}|{email}|{password}\n")
    reset_fields()

def reset_fields():
    website_entry.delete(0, END)
    email_entry.delete(0, END)
    password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)
website_label = Label(text="Website:",justify="left")
website_label.grid(column=0, row=1)
website_entry = Entry(width=39)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email_entry = Entry(width=39)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "email@example.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)


generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=37, command=dialog_box)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()