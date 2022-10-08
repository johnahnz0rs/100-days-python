# Flask application 
from random import randint
from flask import Flask
app = Flask(__name__)

# variables
rand_int = randint(0,9) # random number between 0 and 9



# home route 
@app.route('/')
def home():
    return '<h1>Guess a number between 0 and 9</h1>' \
        '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width="400">'
    


# detect the user's guess e.g "URL/3" or "URL/9" 
@app.route('/<int:guess>')
def guess(guess):
    # checks that number against the generated random number.
    if guess == rand_int:
        # guessed the correct number
        output = f'<div style="text-align: center;"><h1>you guessed right! {guess}</h1><p>way to go mang!</p><img src="https://media.giphy.com/media/WoUynUguj7wEP7HN0T/giphy.gif" width="350"></div>'
        # rand_int = randint(0,10)
    elif guess < rand_int:
        # guess is too low 
        output = f'<div style="text-align: center;"><h1>Your guess is too low</h1><p>you guessed {guess}</p><img src="https://media.giphy.com/media/fqst7AVqF6AVLlYklE/giphy.gif" width="350"><p>guess again {rand_int}</p></div>'
    elif guess > rand_int:
        # guess is too high 
        output = f'<div style="text-align: center;"><h1>yu0r guess is to0 high</h1><p>yu0 gu3ssed {guess}</p><img src="https://media.giphy.com/media/26tPmgvOZmiDXBsyI/giphy.gif" width="350"><p>guess again {rand_int}</p></div>'
    return output

    

    
    # try to make the <h1> text a different colour for each page. e.g. If the random number was 5:




if __name__ == '__main__':
    app.run(debug=True)

