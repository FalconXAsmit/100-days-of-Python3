import tkinter as tk
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pass_letters = random.randint(6, 8)
    pass_numbers = random.randint(1,3)
    pass_symbols = random.randint(1,3)
    password_list = []

    password_letters = [random.choice(letters) for _ in range(pass_letters)]
    password_symbols = [random.choice(symbols) for _ in range(pass_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(pass_numbers)]

    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="OOPS", message="Don't leave any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {email}\nPassword: {password}\nIs it ok to save?")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0,tk.END)
                password_entry.delete(0,tk.END)

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tk.Canvas(width=200, height=200)
logo_img = tk.PhotoImage(file="Projects/Day 029/logo.png")
canvas.create_image(100,100, image=logo_img)
canvas.grid(row=0,column=1)

# Labels
website_label = tk.Label(text="Website:")
website_label.grid(row=1, column=0, sticky="e")

email_label = tk.Label(text="Email/Username:")
email_label.grid(row=2, column=0, sticky="e")

password_label = tk.Label(text="Password:")
password_label.grid(row=3, column=0, sticky="e")

# Entries
website_entry = tk.Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky="ew")
website_entry.focus()

email_entry = tk.Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky="ew")
email_entry.insert(0, "asmit@gmail.com")

password_entry = tk.Entry(width=21)
password_entry.grid(row=3, column=1, sticky="ew")

# Buttons
generate_password_button = tk.Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2, sticky="ew")

add_button = tk.Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="ew")

window.mainloop()