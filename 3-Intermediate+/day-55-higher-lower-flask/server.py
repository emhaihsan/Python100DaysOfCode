from flask import Flask
import random

app = Flask(__name__)

# Generate a random number between 0 and 9
random_number = random.randint(0, 9)

@app.route('/')
def home():
    return '''
    <h1 style="text-align: center;">Guess a number between 0 and 9</h1>
    <img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" style="display: block; margin-left: auto; margin-right: auto;"/>
    '''

@app.route('/<int:guess>')
def guess_number(guess):
    if guess < random_number:
        response = '''
        <h1 style="color: red; text-align: center;">Too low!</h1>
        <img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" style="display: block; margin-left: auto; margin-right: auto;"/>
        '''
    elif guess > random_number:
        response = '''
        <h1 style="color: blue; text-align: center;">Too high!</h1>
        <img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" style="display: block; margin-left: auto; margin-right: auto;"/>
        '''
    else:
        response = '''
        <h1 style="color: green; text-align: center;">You found me!</h1>
        <img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" style="display: block; margin-left: auto; margin-right: auto;"/>
        '''
    return response

if __name__ == "__main__":
    app.run(debug=True)
