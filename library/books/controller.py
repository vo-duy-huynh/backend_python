from flask import Blueprint

books = Blueprint("books", __name__)
@books.route("/get-all-books")
def get_all_books():
    return "All books"