from flask import Flask, render_template
import random
from datetime import date
import requests

app = Flask(__name__)
copyright_year = date.today().year

@app.route('/')
def home():
    rando = random.randint(1,10)
    return render_template("index.html", num=rando, copyright_year=copyright_year)


@app.route('/guess/<string:name>')
def guess(name):
    guess_age = requests.get(url=f"https://api.agify.io/?name={name}")
    guess_gender = requests.get(url=f"https://api.genderize.io/?name={name}")
    age = guess_age.json()["age"]
    gender = guess_gender.json()["gender"]

    return render_template("guess.html", name=name, age=age, gender=gender)


@app.route("/blog")
def blog():
    blog_response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
    posts = blog_response.json()
    return render_template("blog.html", posts=posts)

if __name__ == "__main__":
    app.run(debug=True)

