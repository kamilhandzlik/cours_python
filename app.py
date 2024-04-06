import json
from functools import wraps

from flask import Flask, request

app = Flask(__name__)

USERS = [
    {
        "id":1,
        "username": "Admin",
        "email": "admin@example.com",
        "phoneNumber": 123456789,
}
]

def token_required(func):
    @wraps(func)
    def wrapped_func(*args, **kwargs):
        try:
            token = request.headers["Authorization"]
        except:
            token = None
        if token:
            func(*args, **kwargs)
            return "Authorized", 401

        return wrapped_func


@app.route("/users", methods=["GET", "POST"])
@token_required
def users_crud():
    if request.method == "GET":
        return "Wykonano zadanie przy pomocy metody GET"
    elif request.method == "POST":
        # 1). Validate input
        assert "username" in request.json
        assert "email" in request.json
        assert "phoneNumber" in request.json
        # 2). Save to USERS dict
        user_id = len(USERS) + 1
        user = {"id": user_id, **request.json}
        USERS.append(user)
        return user, 201


@app.route("/users/<int:user_id>", methods=["GET", "PUT", "DELETE", "PATCH"])
@token_required
def specific_user_crud(user_id, token):
    pass


@app.route("/token", methods=["POST"])
def autehnticate_user():
    user = [user for user in USERS if user["username"] ==request.json["username"]][0]
    print(request.json)

    if user:
        if user["password"] == request.json["password"]:
            return json.dumps(
                {
                    "username": user["username"],
                    "permissions": ["WRITE"]
                }
            )



if __name__ == "__main__":
    app.run()
