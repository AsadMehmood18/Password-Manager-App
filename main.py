from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]


    password_list = password_letters+password_symbols+password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    user = user_input.get()
    password = password_input.get()

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_okay = messagebox.askokcancel(title=website, message=f"These are the details entered: \nUser: {user}"
                                                                f" \nPassword: {password} \nIs it okay to save?")
        if is_okay:
            with open("data.txt", mode="a") as data_file:
                data_file.write(f"{website} | {user} | {password}\n")
                website_input.delete(0, END)
                user_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50 , pady=50)
canvas = Canvas(width= 200, height= 200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image= logo_img)
canvas.grid(row= 0, column= 1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row= 1, column=0)
user_label = Label(text="Email/Username:")
user_label.grid(row= 2, column=0)
password_label = Label(text="Password:")
password_label.grid(row= 3, column=0)

# Entries
website_input = Entry(width= 35)
website_input.grid(row= 1, column=1, columnspan= 2)
website_input.focus()
user_input = Entry(width= 35)
user_input.grid(row= 2, column=1, columnspan= 2)
user_input.insert(0, "user@email.com")
password_input = Entry(width= 21)
password_input.grid(row= 3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row= 3, column=2)
add = Button(text= "Add", width= 36, command=save)
add.grid(row= 4, column=1, columnspan= 2)

window.mainloop()