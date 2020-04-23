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


    @app.route('/movies', methods=["POST", "OPTIONS"])
    def post_movie():
        try:
            body = request.get_json()
            new_movie_title = body.get("title", None)
            new_movie_release_date = body.get("release_date", None)
            new_movie_cast_filled = body.get("cast_filled", None)

            movie_new = Movie(title=new_movie_title, release_date=new_movie_release_date, cast_filled=new_movie_cast_filled)
            
            movie_new.insert()

            movie = Movie.query.filter(Movie.title==new_movie_title).one_or_none()
            response = {
                "success": True,
                "id": movie.__dict__["id"],
                "title": movie.__dict__["title"],
                "release_date": movie.__dict__["release_date"],
                "cast_filled": movie.__dict__["cast_filled"]
            }
            return (jsonify(response), 201)
        except:
            abort(422)

    @app.route("/movies/<int:movie_id>", methods=["DELETE"])
    def delete_movie(movie_id):
        try:
            delete_movie = Movie.query.filter(Movie.id==movie_id).one_or_none()
            if delete_movie is None:
                abort(404)
            else:    
                delete_movie.delete()
                return jsonify({"success": True, "deleted": movie_id})
        except:
            abort(404)

    @app.route("/actors")
    def get_actors():
        try:
            actors = Actor.query.order_by(Actor.id).all()
            results = []

            for actor in actors:
                actor_data = {
                    "id": actor.__dict__["id"],
                    "name": actor.__dict__["name"],
                    "age": actor.__dict__["age"],
                    "gender": actor.__dict__["gender"],
                    "seeking_role": actor.__dict__["seeking_role"]
                }
                results.append(actor_data)

            response = {
                "success": True,
                "actors": results
            }
            return jsonify(response)
        except:
            abort(404)

    @app.route('/actors', methods=["POST", "OPTIONS"])
    def post_actor():
        try:
            body = request.get_json()
            new_actor_name = body.get("name", None)
            new_actor_age = body.get("age", None)
            new_actor_gender = body.get("gender", None)
            new_actor_seeking_role = body.get("seeking_role", None)

            actor_new = Actor(name=new_actor_name, age=new_actor_age, gender=new_actor_gender, seeking_role=new_actor_seeking_role)
            
            actor_new.insert()

            actor = Actor.query.filter(Actor.name==new_actor_name).one_or_none()
            response = {
                "success": True,
                "id": actor.__dict__["id"],
                "name": actor.__dict__["name"],
                "age": actor.__dict__["age"],
                "gender": actor.__dict__["gender"],
                "seeking_role": actor.__dict__["seeking_role"]
            }
            return (jsonify(response), 201)
        except:
            abort(422)

    @app.route("/actors/<int:actor_id>", methods=["DELETE"])
    def delete_actor(actor_id):
        try:
            delete_actor = Actor.query.filter(Actor.id==actor_id).one_or_none()
            if delete_actor is None:
                abort(404)
            else:    
                delete_actor.delete()
                return jsonify({"success": True, "deleted": actor_id})
        except:
            abort(404)

    @app.route('/casts')
    def get_casts():
        try:
            movies = Movie.query.order_by(Movie.id).all()
            results = []
            for movie in movies:
                cast_data = {
                    "movie_id": movie.__dict__["id"],
                    "movie_title": movie.__dict__["title"],
                    "release_date": movie.__dict__["release_date"],
                    "cast": []
                }
                casts = CastMember.query.filter(CastMember.movie_id==movie.__dict__["id"]).all()
                for cast_member in casts:
                    actor = Actor.query.filter(Actor.id==cast_member.__dict__["actor_id"]).one_or_none()
                    cast_data["cast"].append({actor.__dict__["id"]: actor.__dict__["name"]})

                results.append(cast_data)
            response = {
                "success": True,
                "casts": results
            }
            return jsonify(response)
        except:
            abort(404)

    @app.route('/casts', methods=["POST", "OPTIONS"])
    def post_cast_member():
        try:
            body = request.get_json()
            new_cast_movie_id = body.get("movie_id", None)
            new_cast_actor_id = body.get("actor_id", None)

            cast_new = CastMember(movie_id=new_cast_movie_id, actor_id=new_cast_actor_id)
            
            cast_new.insert()

            cast = CastMember.query.filter(CastMember.movie_id==new_cast_movie_id).one_or_none()
            response = {
                "success": True,
                "id": cast.__dict__["id"],
                "movie_id": cast.__dict__["movie_id"],
                "actor_id": cast.__dict__["actor_id"]
            }
            return (jsonify(response), 201)
        except:
            abort(422)

    @app.route("/casts/<int:cast_id>", methods=["DELETE"])
    def delete_cast_member(cast_id):
        try:
            delete_cast_member = CastMember.query.filter(CastMember.id==cast_id).one_or_none()
            if delete_cast_member is None:
                abort(404)
            else:    
                delete_cast_member.delete()
                return jsonify({"success": True, "deleted": cast_id})
        except:
            abort(404)

    return app