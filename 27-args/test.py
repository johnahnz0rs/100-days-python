import tkinter

def button_clicked():
    my_label.config(text="I got clicked")

def new_button_clicked():
    print("johnahnz0rs is l33t")
    print(my_entry_value.get())


# window
window = tkinter.Tk()
window.title("LOL")
window.minsize(width=500, height=300)

# label
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.grid(row=0, column=0)



# button
button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(row=1, column=1)


# new_button
new_button = tkinter.Button(text="new button", command=new_button_clicked)
new_button.grid(row=0, column=2)

# entry/input
my_entry_value = tkinter.StringVar(value="blah blah blah")
my_entry = tkinter.Entry(window, textvariable=my_entry_value, width=100)
my_entry.grid(row=2, column=3)



window.mainloop()
