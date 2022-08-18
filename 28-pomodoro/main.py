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







# the assignment
# the assignment
# the assignment
'''
1. pomodoro goes 8 rounds; use a round counter
2. on the 8th round, the timer is 20 [1 x 25, 1 x 5, ... , 1 x 20]
3. for all rounds
    a. increase round counter
    b. countdown appropriate time
    b. update the title label

'''


round_counter = 1

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    pass
    # countdown(250)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global title_label
    title_label.config(text="WORK", fg=GREEN)
    countdown(5)
    # countdown(250)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global round_counter

    # format & print remaining time
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    new_count = 0
    if count > 0:
        new_count = count - 1
        # window.after(1000, countdown, count-1)
        print(f"{count} - continue countdown")
    else:
        
        print(f"------------just finished round {round_counter}")
        round_counter += 1
        print(f"------------now starting round {round_counter}")
        # reached 0:00 - change round

        update_title_label(round_counter)
        if round_counter % 2 == 0:
            # this is a REST round
            add_checkmark()
            if round_counter % 8 == 0:
                # this is a long rest = 20 min
                new_count = LONG_BREAK_MIN
            else:
                # this is a short rest = 5 min
                new_count = SHORT_BREAK_MIN
        else:
            # this is WORK = 25 min
            new_count = WORK_MIN
        
    window.after(1000, countdown, new_count)


def add_checkmark():
    global checkmarks
    global checkmarks_text
    global lol
    checkmarks_text += lol
    checkmarks.config(text=checkmarks_text)

def update_title_label(round):
    global title_label
    if round % 8 == 0:
        new_title = "REST"
        title_color = PINK
    elif round % 2 == 0:
        new_title = "REST"
        title_color = RED
    else:
        new_title = "WORK"
        title_color = GREEN
    title_label.config(text=new_title, fg=title_color)




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
# lol = "✓"
lol = "✅"
checkmarks_text = ""
checkmarks = Label(text=checkmarks_text, fg=GREEN, bg=YELLOW)
checkmarks.grid(column=1, row=3)



window.mainloop()

