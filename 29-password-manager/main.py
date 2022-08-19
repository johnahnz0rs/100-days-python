# the assignment
# the assignment
# the assignment

# 1. 3 cols, 5 rows
# 2. rows: 
    # a. logo image 
    # b. website -- input width:35, spans 2 cols 
    # c. email/username -- input width:35, spans 2 cols
    # d. password -- input width:21 && generate password button in 3rd col
    # e. add -- button to store the new tuple (write to a file)


# imports and constants
# imports and constants
# imports and constants
from email import message
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

BLACK = "#000"
# FONT = ("Courier", 14, "bold")
FONT = ("Arial", 14, "bold")
CENTER = "center"


window = Tk()
# window.minsize(width=600, height=500)
window.config(padx=50, pady=50)
window.title("Password Manager")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pw_letters = [choice(letters) for _ in range(randint(8, 10))]
    pw_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    pw_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = pw_letters + pw_numbers + pw_symbols

    shuffle(password_list)

    password = "".join(password_list)

    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)

    messagebox.showinfo(title="Password Manager", message="Password copied to clipboard.")



# ---------------------------- SAVE PASSWORD ---------------------
def save():
    website = website_val.get().strip()
    email = email_val.get().strip()
    password = password_val.get().strip()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Password Manager", message="Please enter a value for every field")
    else:
        ok_to_save = messagebox.askokcancel(title=f"{website}", message=f"ok to save? \nemail/username: {email} \npassword: {password}")
        if ok_to_save:
            with open("data.txt", mode="a") as data:
                data.write(f"{website} | {email} | {password}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)




# ---------------------------- UI SETUP ------------------------------- #

# logo canvas
canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(90, 90, image=logo)
canvas.grid(column=1, row=0)

# website label
website_label = Label(text="Website:", fg=BLACK, font=FONT)
website_label.grid(column=0, row=1)

# website input
website_val = StringVar(value="")
website_input = Entry(textvariable=website_val, width=39)
website_input.grid(column=1, row=1, columnspan=2, sticky="w")
website_input.focus()

# email/username label
email_label = Label(text="Email/Username:", fg=BLACK, font=FONT)
email_label.grid(column=0, row=2)

# email input
email_val = StringVar(value="")
email_input = Entry(textvariable=email_val, width=39)
email_input.insert(0, "test@gmail.com")
email_input.grid(column=1, row=2, columnspan=2, sticky="w")

# password label
password_label = Label(text="Password:", fg=BLACK, font=FONT)
password_label.grid(column=0, row=3)

# password input
password_val = StringVar(value="")
password_input = Entry(textvariable=password_val, width=21)
password_input.grid(column=1, row=3, sticky="w")

# generate password button
gen_pass_button = Button(text="Generate password", highlightthickness=0, command=generate_password)
gen_pass_button.grid(column=2, row=3)

# add button
add_button = Button(text="Add", width=37,  highlightthickness=0, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="w")



window.mainloop()



