from password_gen import PasswordGenerator
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pyperclip
import json

DEFAULT_EMAIL = "email@email.com"


# ---------------------------- Backend ------------------------------- #

# Get file keys and save as options list
options = []

try:
    with open("data.json", "r") as data_file:
        data = json.load(data_file)
        for k, v in data.items():
            options.append(k)
except FileNotFoundError:
    pass


# Generate and update password
def update_password():
    password_generator = PasswordGenerator()
    password = password_generator.generate_password()
    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)


# Save data to file and clear non default entries
def save():
    website_text = website_input.get()
    username_text = username_input.get()
    password_text = password_input.get()

    new_data = {
        website_text: {
            "email": username_text,
            "password": password_text
        }
    }

    if len(website_text) == 0 or len(password_text) == 0:
        messagebox.showerror(
            title="PassBox", message="Please don't leave any fields empty!")
        return
    else:
        is_ok = messagebox.askokcancel(
            title="PassBox", message=f"Your entered details: \nEmail: {username_text}\nPassword: {password_text}\nDo you want to save?")

    if is_ok:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        website_input.delete(0, END)
        password_input.delete(0, END)
        options.append(website_text)


def search():
    website = dropdown_menu.get()
    with open("data.json", "r") as data_file:
        data = json.load(data_file)
        try:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(
                title="PassBox", message=f"Email: {email}\nPassword: {password}")
        except KeyError:
            messagebox.showerror(
                title="PassBox", message=f"No details for {website} exists.")


# ---------------------------- UI ------------------------------- #
# Window
root = Tk()
root.title("PassBox")
root.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
dropdown_label = Label(text="Select a site:")
dropdown_label.grid(row=2, column=0)
username_label = Label(text="Email/Username:")
username_label.grid(row=3, column=0)
password_label = Label(text="Password:")
password_label.grid(row=4, column=0)

# Entries
website_input = Entry(width=38)
website_input.focus()
website_input.grid(row=1, column=1, columnspan=2)
dropdown_menu = ttk.Combobox(
    value=options, width=19, postcommand=lambda: dropdown_menu.configure(values=options))
dropdown_menu.grid(row=2, column=1)
username_input = Entry(width=38)
username_input.insert(0, DEFAULT_EMAIL)
username_input.grid(row=3, column=1, columnspan=2)
password_input = Entry(width=21)
password_input.grid(row=4, column=1)

# Buttons
search_button = Button(text="Search", width=13, command=search)
search_button.grid(row=2, column=2)
gen_pass_button = Button(text="Generate Password",
                         command=update_password)
gen_pass_button.grid(row=4, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=5, column=1, columnspan=2)

root.mainloop()
