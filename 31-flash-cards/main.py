# johnahnz0rs is l33t

# imports and constants
# imports and constants
# imports and constants
from tkinter import *
import pandas as pd
from random import choice
BACKGROUND_COLOR = "#B1DDC6"


# functionality
# functionality
# functionality
french_words = pd.read_csv("data/french_words.csv")
french_words = french_words.to_dict(orient="records")
# print(french_words)

def clicked_wrong():
    # pass
    get_new_word()

def clicked_right():
    # pass
    get_new_word()

def get_new_word():
    new_dict = choice(french_words)
    new_french = new_dict["French"]
    new_english = new_dict["English"]
    canvas.itemconfig(canvas_title, text="French")
    canvas.itemconfig(canvas_word, text=new_french)
    print(new_dict)








# UI
# UI
# UI
window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flashy")
window.geometry("900x726+30+30")

img_card_front = PhotoImage(file="images/card_front.png")
canvas = Canvas(height=526, width=800)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=img_card_front)

canvas_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
canvas_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# label_language = Label()
# label_language.grid()

# label_word = Label()

# img_card_back = PhotoImage(file="images/card_back.png")

img_wrong = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=img_wrong, highlightthickness=0, command=clicked_wrong)
button_wrong.grid(column=0, row=1)

img_right = PhotoImage(file="images/right.png")
button_right = Button(image=img_right, highlightthickness=0, command=clicked_right)
button_right.grid(column=1, row=1)







window.mainloop()
