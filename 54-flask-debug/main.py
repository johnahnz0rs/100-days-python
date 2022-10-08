from flask import Flask
app = Flask(__name__)


# decorators
# decorators
# decorators
def make_bold(function):
    def wrapper():
        return f"<b>{ function() }</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return f"<em>{ function() }</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return f"<u>{ function() }</u>"
    return wrapper


# routes
# routes
# routes
@app.route('/')
def hello_world():
    return '<h1>Hellow World</h1>' \
        '<p>this is a paragraph.</p>' \
        '<img src="https://media.giphy.com/media/5nh8FKSRtxFEyuajGc/giphy.gif" width="200">'

@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye"

@app.route('/username/<name>/<int:number>')
def greet(name, number):
    return f"Hello there {name}, you are {number+2} years old!!"



# run it
if __name__ == "__main__":
    app.run(debug=True)



