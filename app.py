from flask import Flask, render_template, session, redirect, url_for
import os
import random

random_number = random.randint(0, 9)

app = Flask(__name__)
import os
app.secret_key = os.environ.get('SECRET_KEY')


# Home Page
@app.route('/')
def home():
    # Generate and store a new random number in the session
    session['random_number'] = random.randint(0, 9)
    return render_template("home.html")
    

# Users Guess
@app.route('/<int:number>')
def users_guess(number):
    random_number = session.get('random_number')  # Get number from session
    if random_number is None:
        return redirect(url_for('home'))  # If session expired or missing, reset

    if number == random_number:
        return render_template("you_found_me.html")
    elif number < random_number:
        return render_template("too_low.html")
    else:
        return render_template("too_high.html")

# Hidden player name easter egg
@app.route('/<string:name>')
def easter_egg(name):
    return render_template('easter_egg.html', name=name)

# Debug route
@app.route('/show_random_number')
def show_random_number():
    return f"Random number in session is: {session.get('random_number')}"



if __name__ == "__main__":
    app.run(debug=True)