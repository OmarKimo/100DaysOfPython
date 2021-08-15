from flask import Flask
from random import randint as rnd

app = Flask(__name__)

number = rnd(0, 9)

@app.route('/')
def hello_world():
    global number
    number = rnd(0, 9)
    return '<h1>Guess a number between 0 and 9</h1>' \
    '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" alt="number gif"/>'

@app.route("/<int:guess>")
def check_guess(guess):
    global number
    if guess < number:
        return "<h1 style='color:red'>Too low, try again!</h1>" \
            '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" alt="too low gif"/>'
    elif guess > number:
        return "<h1 style='color:purple'>Too high, try again!</h1>" \
            '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" alt="too low gif"/>'
    else:
        return "<h1 style='color:green'>You found me!</h1>" \
            '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" alt="too low gif"/>'

if __name__ == "__main__":
    app.run(debug=True)
