from flask import Flask, request

app = Flask(__name__)


@app.route("/users", methods=["GET", "POST"])
def users_crud():
    if request.method == "GET":
        return "Wykonano zadanie przy pomocy metody GET"
    elif request.method == "POST":
        return "Wykonano zadanie przy pomocy metody POST"


if __name__ == "__main__":
    app.run()
