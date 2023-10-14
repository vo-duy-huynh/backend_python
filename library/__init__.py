from flask import Flask, request, Blueprint, jsonify
from .books.controller import books
def create_app(config_file="config.py"):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)

    app.register_blueprint(books)
    # app.register_blueprint(library, url_prefix='/library')
    return app