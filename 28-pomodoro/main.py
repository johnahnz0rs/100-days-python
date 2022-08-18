from tkinter import *
import math


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
round_counter = 0
timer = None



# the assignment
'''
1. pomodoro goes 8 rounds; use a round counter
2. on the 8th round, the timer is 20 [1 x 25, 1 x 5, ... , 1 x 20]
3. for all rounds
    a. increase round counter
    b. countdown appropriate time
    b. update the title label

'''

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    # reset title_label, checkmarks, time, round_counter
    window.after_cancel(timer)
    global round_counter
    round_counter = 0
    title_label.config(text="TIMER", fg="#000")
    checkmarks_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    # how many checkmarks?
    global round_counter
    round_counter += 1
    how_many_checks = math.floor(round_counter / 2)
    checks_text = ""
    for _ in range(how_many_checks):
        checks_text += "✅"
    checkmarks_label.config(text=checks_text)

    # determine action based on round: update title_label, start new countdown
    if round_counter % 8 == 0:
        title_label.config(text="REST", fg=RED)
        # countdown(LONG_BREAK_MIN * 60)
        countdown(20)
    elif round_counter % 2 == 0:
        title_label.config(text="REST", fg=PINK)
        # countdown(SHORT_BREAK_MIN * 60)
        countdown(5)
    else:
        title_label.config(text="WORK", fg=GREEN)
        # countdown(WORK_MIN * 60)
        countdown(10)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    # format & print remaining time
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    # next step
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
# ---------------------------- UI SETUP ------------------------------- #
# ---------------------------- UI SETUP ------------------------------- #

# window
window = Tk()
window.config(padx=100, pady=50, bg=YELLOW)
window.title("Pomodoro")

# tomato canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# title label
title_label = Label(text="Timer", fg="#000", bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

# start button
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

# reset button
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# checkmarks
checkmarks_label = Label(text="", fg=GREEN, bg=YELLOW)
checkmarks_label.grid(column=1, row=3)

window.mainloop()

