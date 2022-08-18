from textwrap import fill
from tkinter import *


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    pass

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    pass

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=100, pady=50, bg=YELLOW)
window.title("Pomodoro")

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
# canvas.pack()
canvas.grid(row=1, column=1)

title_label = Label(text="Timer", bg=YELLOW)
title_label.grid(row=0, column=1)


start_button = Button(window, text="Start", command=start_timer, fg=GREEN, bg="red")
start_button.grid(row=2, column=0)


reset_button = Button(window, text="Reset", command=reset_timer)
reset_button.grid(row=2, column=2)

lol = "✓"
check_mark = Label(text="✓")
check_mark.grid(row=2, column=1)



window.mainloop()

