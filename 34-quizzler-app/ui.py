from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Text(wid)

        self.canvas = Canvas(height=250, width=300)
        self.canvas.config(bg="white", highlightthickness=0)
        self.question = self.canvas.create_text(150, 125, text="lololol", font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2)




        self.window.mainloop()