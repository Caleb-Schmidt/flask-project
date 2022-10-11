from flask import Flask, render_template

app = Flask(__name__)

@app.route('/homepage')
def homepage():
    return render_template("homepage.html.j2")

@app.route('/pokemon')
def pokemon():
    return render_template("pokemon.html.j2")