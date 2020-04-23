import os
from flask import Flask, request, abort, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from models import setup_db, Movie, Actor, CastMember, db

def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type, Authorization, true"
        )
        response.headers.add(
            "Access-Control-Allow-Methods", "GET, DELETE, POST, OPTIONS"
        )
        response.headers.add("Access-Control-Allow-Credentials", "true")
        return response

    @app.route('/')
    def index():
        return 'Working'


    @app.route('/movies')
    def get_movies():
        try:
            movies = Movie.query.order_by(Movie.id).all()
            print(movies)
            results = []

            for movie in movies:
                movie_entry = {
                    "id": movie.__dict__["id"],
                    "title": movie.__dict__["title"],
                    "release_date": movie.__dict__["release_date"],
                    "cast_filled": movie.__dict__["cast_filled"]
                }
                results.append(movie_entry)

            response = {
                "success": True,
                "movies": results
            }
            return jsonify(response)
        except:
            abort(404)
    return app