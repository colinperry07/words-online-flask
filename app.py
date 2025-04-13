from flask import Flask, render_template, request, redirect, session
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
    
    if "streak" not in session:
        session["streak"] = 0
    if "solved" not in session:
        session["solved"] = False
    if "incorrect" not in session:
        session["incorrect"] = False
    
    if request.method == "POST":
        user_guess = request.form.get("guess")
        actual_word = session.get("actual_word")
        if actual_word and check_guess(actual_word, user_guess):
            session["streak"] += 1
            session["incorrect"] = False
            session["solved"] = True
            return redirect("/")
        else:
            session["streak"] = 0
            session["incorrect"] = True
            session["solved"] = False
            return redirect("/")

    if request.method == "GET":
        
        if session.get("solved"):
            new_word = pick_random_word()
            session["actual_word"] = new_word
            session["jumbled_word"] = jumble_word(new_word)
            session["solved"] = False
            return render_template("index.html", jumbled_word=session["jumbled_word"], message="Correct!", streak=session["streak"])
        
        if session.get("incorrect"):
            return render_template("index.html", jumbled_word=session["jumbled_word"], message="Try Again!")
        
        else:
            return render_template("index.html", jumbled_word=session["jumbled_word"])

    session["incorrect"] = False
    word = pick_random_word()
    session["actual_word"] = word
    session["jumbled_word"] = jumble_word(word)
    return render_template("index.html", jumbled_word=session["jumbled_word"])

@app.route("/new")
def new_word():
    word = pick_random_word()
    session["actual_word"] = word
    session["jumbled_word"] = jumble_word(word)
    session["solved"] = False
    session["incorrect"] = False
    return redirect("/")
