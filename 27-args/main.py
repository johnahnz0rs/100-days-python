from tkinter import *


def calculate_km():
    mi = float(input_miles_val.get())
    km = "{:.2f}".format(mi * 1.609)
    label_km_converted.config(text=km)

# window.title
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# row 1
input_miles_val = StringVar(value=0)
input_miles = Entry(window, textvariable=input_miles_val, width=7)
input_miles.grid(row=0, column=1)

label_miles = Label(text="Miles")
label_miles.grid(row=0, column=2)

# row 2
label_equal = Label(text="is equal to")
label_equal.grid(row=1, column=0)

label_km_converted = Label(text="0")
label_km_converted.grid(row=1, column=1)

label_km = Label(text="Km")
label_km.grid(row=1, column=2)

# row 3
calc_button = Button(text="Calculate", command=calculate_km)
calc_button.grid(row=2, column=1)




window.mainloop()
