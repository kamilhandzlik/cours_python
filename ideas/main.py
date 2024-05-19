from flask import Flask, request, jsonify
from flask.views import View, MethodView
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity,
)
from datetime import timedelta
from flask_restful import Api, Resource


app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "Secret"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(seconds=10)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=1)
jwt = JWTManager(app)

items = [{id: f"id: {id} id"} for id in range(15)]
books = [{id: f"Ksiazka: {id}"} for id in range(15)]
movies = [{id: f"Film: {id}"} for id in range(15)]

database = {"items": items, "books": books, "movies": movies}


@app.route("/token", methods=["POST"])
def token():
    username = request.json.get("username", "")
    password = request.json.get("password", "")

    if username == "admin" and password == "1234":
        access_token = create_access_token(
            identity=username,
        )
        refresh_token = create_refresh_token(identity=username)
        return jsonify({"access_token": access_token, "refresh_token": refresh_token})

    return jsonify({"message": "Wrong username or password"}), 401


@app.route("/token/refresh")
@jwt_required(refresh=True)
def refresh():
    identity = get_jwt_identity()
    new_token = create_access_token(identity=identity)
    return jsonify({"access_token": new_token})


class PaginatedView(View):
    methods = ["POST", "GET"]

    def __init__(self, model):
        self.model = model
        self.items = database[model]

    def dispatch_request(self):
        if request.method == "GET":
            page = request.args.get("page", 1, type=int)
            per_page = request.args.get("per_page", 5, type=int)

            start = (page - 1) * per_page
            end = start + per_page
            result = self.items[start:end]

            return jsonify({"total": len(self.items), "items": result})
        elif request.method == "POST":
            pass


class Books(MethodView):
    decorators = [jwt_required()]

    def __init__(self, model):
        self.model = model
        self.items = database[model]

    def get(self):
        page = request.args.get("page", 1, type=int)
        per_page = request.args.get("per_page", 5, type=int)

        start = (page - 1) * per_page
        end = start + per_page
        result = self.items[start:end]

        return jsonify({"total": len(self.items), "items": result})

    def post(self):
        new_book_name = request.json["name"]
        new_book = {"id": len(self.items) + 1, "name": new_book_name}
        database["books"].append(new_book)
        return new_book, 201


class ProtectedPaginatedView(PaginatedView):
    decorators = [jwt_required()]


app.add_url_rule(
    "/books",
    view_func=Books.as_view("paginated_books_view", model="books"),
)
app.add_url_rule(
    "/movies", view_func=PaginatedView.as_view("paginated_movies_view", model="movies")
)
app.add_url_rule(
    "/items", view_func=PaginatedView.as_view("paginated_items_view", model="items")
)



@app.route("/token", methods=["POST"])
def token():
    username = request.json["username", ""]
    password = request.json["password", ""]

    if username == "admin" or password == "1234":
        token = create_access_token(
            identity=username,
            additional_claims = {'permissions':['READ', 'WRITE' 'DELETE']}
        )
        refresh_token = create_access_token(identity=username)
        return jsonify({'access token':token, 'refresh token':refresh_token}), 200

    return  jsonify({"message": "Wrong username or password"}), 401
@app.route("/token/refresh")
@jwt_required(refresh=True)
def refresh():
    identity = get_jwt_identity()
    new_token = create_access_token(identity=identity)
    return jsonify({'access token':new_token}), 200

@app.route("/hello")
def index1():
    name = request.args.get("name", '')
    age = request.args.get("age", '')

    return f"Hello, {name}. You are {age} years old!"

@app.route("/items")
def index2():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 5, type=int)

    start = (page - 1) * per_page
    end = page * per_page

    result = items[start:end]

    return jsonify(
        {
            "items":result,
            "total":len(items),
            "next":f"https//:localhost:5000/items?page={page+1}"
        }
    )

##############################################
#---------------- Flask restful API ---------#
##############################################

books = []

class Book:
    def __init__(self, name, author):
        self.id = len(books) + 1
        self.name = name
        self.author = author

books += [Book(name=f"Książka {num}", author="Example author") for num in range(15)]


class BookDetail(Resource):
    def _get_book(self, id):
        book = next(filter(lambda book: book.id == id, books), None)
        if book:
            return {"id":book.id, "name":book.name, "author":book.author}
        return {"message":"Book not found"}, 400

    def patch(self):
        book = request.get_book(id)
        author = request.json["author"]



# @app.route("/tokenbook", methods=["POST"])
# def tokenbook():



if __name__ == '__main__':
    app.run(debug=True)

