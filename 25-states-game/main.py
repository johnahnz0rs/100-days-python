# convert the guess to title case
# check if the guess is among the 50 states
# write correct guesses on the map
# use a loop to allow the user to keep guessing
# record the correct guesses in a list
# keep track of the score

# imports and vars
import turtle
import pandas
FONT = ("Courier", 12, "normal")
ALIGNMENT = "center"
correct_guesses = []


# set up us the screen
screen = turtle.Screen()
screen.title("50 States Game")
image = "blank_states_img.gif"
screen.bgpic(image)

# get the states
df = pandas.read_csv("50_states.csv")  
states = df["state"].to_list()


# create the writer(Turtle)
labels = turtle.Turtle()
labels.penup()
labels.hideturtle()
def write_state_label(state, coord):
    labels.goto(coord)
    labels.write(state, font=FONT, align=ALIGNMENT)



# gameplay
while len(correct_guesses) < 50:
    # make a guess
    guess = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct", prompt="Name a state").title()
    # secret command to exit
    if guess == "Exit":
        missing_states = [s for s in states if s not in correct_guesses]
        output = pandas.DataFrame(missing_states)
        output.to_csv("missing_states.csv")
        break
    # if guess is correct like a mafuqa
    if guess not in correct_guesses and guess in states:
        correct_guesses.append(guess)
        state_info = df[df["state"] == guess]
        write_state_label(guess, (int(state_info["x"]), int(state_info["y"])))


# screen.exitonclick()
