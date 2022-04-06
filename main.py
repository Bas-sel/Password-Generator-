from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generator():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for letter in range(nr_letters)]

    password_numbers = [random.choice(numbers) for number in range(nr_numbers)]

    password_symbols = [random.choice(symbols) for symbol in range(nr_symbols)]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)
    password = ''.join(password_list)

    password_entry.insert(END, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_button():
    if website_entry.get() == '' or email_entry.get() == '' or password_entry.get() == '':
        messagebox.showwarning(title="Warning", message="Please don't leave any field empty")

    else:
        confirm = messagebox.askokcancel(title=website_entry.get(),
                                         message=f'Entered details \nEmail: {email_entry.get()}\n'
                                                 f'Password: {password_entry.get()}\n')
        if confirm:
            with open('file.txt', mode='a') as data:
                data.write(f'{website_entry.get()} : | {email_entry.get()}  | {password_entry.get()}\n')
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
photo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=photo)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=2)

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=40)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

email_entry = Entry(width=40)
email_entry.insert(END, 'example@example.com')
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=22)
password_entry.grid(column=1, row=3)

# Buttons

generate_password = Button(text='Generate Password',command=generator)
generate_password.grid(column=2, row=3, columnspan=1)

add = Button(width=35, text='ADD', command=add_button)
add.grid(column=1, row=4, columnspan=2)

window.mainloop()
