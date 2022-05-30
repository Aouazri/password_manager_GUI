from tkinter import *
# messagebox is another module of code
from tkinter import messagebox
from random import choice, randint, shuffle
# import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for char in range(randint(8, 10))]

    password_symbols = [choice(symbols) for char in range(randint(2, 4))]

    password_numbers = [choice(numbers) for char in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    # join method
    password = "".join(password_list)
    password_entry.insert(0, password)
    # pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(password) == 0 or len(website) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")
    else:
        confirm = messagebox.askokcancel(title=website, message=f"There are the details entered: \nEmail: {email}"
                                                                f"\nPassword: {password} \nIs it ok to save?")
        if confirm:
            with open("data.txt", mode='a') as f:
                f.write(f"{website} | {email} | {password} \n")
                website_entry.delete(0, 'end')
                password_entry.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
# window.minsize(width=300, height=250)
window.config(padx=20, pady=20)
# Canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)

canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website")
email_label = Label(text="Email/Username")
password_label = Label(text="Password")

website_label.grid(column=0, row=1)
email_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)
# Entries
website_entry = Entry(width=35)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.insert(END, "fenyegol47@gmail.com")
password_entry = Entry(width=17)

website_entry.grid(column=1, row=1, columnspan=2)
email_entry.grid(column=1, row=2, columnspan=2)
password_entry.grid(column=1, row=3)
# Buttons
add_button = Button(text="Add", width=36, command=save)
generate_button = Button(text="Generate Password", command=generate_password)

generate_button.grid(column=2, row=3)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
