# 2. Create a new Flask application 
from random import randrange
from flask import Flask
app = Flask(__name__)
# rand_int = randrange(0,10)
RAND_INT = randrange(0,10)


# where the home route 
@app.route('/')
def home():
    # displays an <h1> that says "Guess a number between 0 and 9" 
    # and display https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif
    return '<h1>Guess a number between 0 and 9</h1>' \
        '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width="400">'
    

# 3. Generate a random number between 0 and 9 or any range of numbers of your choice.
# rand_int = randrange(0,10)
# print(f"rand_int: {rand_int}")


# 4. Create a route that can detect the number entered by the user e.g "URL/3" or "URL/9" 
@app.route('/guess/<int:i>')
def guess(i):
    # return f'<p>rand_int: {rand_int}</p><p>i (from url): {i}</p>'
    return f'<p>rand_int: {RAND_INT}</p><p>i (from url): {i}</p>'


    # and checks that number against the generated random number. 
    # If the number is too low, tell the user it's too low, https://media.giphy.com/media/fqst7AVqF6AVLlYklE/giphy.gif
    # same with too high https://media.giphy.com/media/26tPmgvOZmiDXBsyI/giphy.gif
    # or if they found the correct number. https://media.giphy.com/media/WoUynUguj7wEP7HN0T/giphy.gif

    
    # try to make the <h1> text a different colour for each page. e.g. If the random number was 5:




if __name__ == '__main__':
    app.run(debug=True)

