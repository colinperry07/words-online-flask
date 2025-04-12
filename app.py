from flask import Flask, render_template, request, redirect, session, url_for
from gamelogic import pick_random_word, jumble_word, check_guess

app = Flask(__name__)
app.secret_key = 'abcdefghijklmnopqrstuvwxyz'


# for future reference colin (for @app.route() functions):
# get - accessing data
# post - sending data
# put - updating data
# delete -removing data

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_guess = request.form.get("guess")
        actual_word = session.get("actual_word")
        if actual_word and check_guess(actual_word, user_guess):
            session["streak"] += 1
            return render_template("index.html", jumbled_word=session["jumbled_word"], message="Correct!", streak=session["streak"])
        else:
            session["streak"] = 0
            return render_template("index.html", jumbled_word=session["jumbled_word"], message="Try Again!")

    session["streak"] = 0
    word = pick_random_word()
    session["actual_word"] = word
    session["jumbled_word"] = jumble_word(word)
    return render_template("index.html", jumbled_word=session["jumbled_word"])