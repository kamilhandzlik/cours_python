from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("hello.html")


@app.route("/cokolwiek")
def cokolwiek():
    return "<h1>Let the bodies hit the floor</h1>"


@app.route("/liczba/<int:liczba>")
def trasa_liczba(liczba):
    return f"<h1>Wybrana liczba to: {liczba}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
