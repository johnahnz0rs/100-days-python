# johnahnz0rs is l33t

# imports and constants
# imports and constants
# imports and constants
from tkinter import *
import pandas as pd
from random import choice
BACKGROUND_COLOR = "#B1DDC6"

try:
    df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv("data/french_words.csv")
finally:
    french_words = df.to_dict(orient="records")
    current_card = {}



# functionality
# functionality
# functionality

def clicked_wrong():
    new_card()

def clicked_right():
    global current_card
    french_words.remove(current_card)
    to_learn = pd.DataFrame.from_records(french_words)
    to_learn.to_csv("data/words_to_learn.csv", index=False)
    new_card()

def new_card():
    global current_card
    current_card = choice(french_words)
    canvas.itemconfig(canvas_background, image=img_card_front)
    canvas.itemconfig(canvas_title, text="French", fill="black")
    canvas.itemconfig(canvas_word, text=current_card["French"], fill="black")
    window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(canvas_background, image=img_card_back)
    canvas.itemconfig(canvas_title, text="English", fill="white")
    canvas.itemconfig(canvas_word, text=current_card["English"], fill="white")

def learned_a_word(flashcard):
    global french_words
    








# UI
# UI
# UI
window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flashy")
window.geometry("900x726+30+30")

img_card_front = PhotoImage(file="images/card_front.png")
img_card_back = PhotoImage(file="images/card_back.png")
canvas = Canvas(height=526, width=800)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_background = canvas.create_image(400, 263, image=img_card_front)

canvas_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
canvas_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# label_language = Label()
# label_language.grid()

# label_word = Label()


img_wrong = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=img_wrong, highlightthickness=0, command=clicked_wrong)
button_wrong.grid(column=0, row=1)

img_right = PhotoImage(file="images/right.png")
button_right = Button(image=img_right, highlightthickness=0, command=clicked_right)
button_right.grid(column=1, row=1)





# run da program
# run da program
# run da program

window.after(3000, func=flip_card)

new_card()

window.mainloop()
