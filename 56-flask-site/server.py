from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def homepage():
    # return 'hellowworld'
    # return render_template('index.html')
    # return render_template('johnahn.html')
    # return render_template('cv.html')
    return render_template('paradigm.html')


if __name__ == '__main__':
    app.run(debug=True)

