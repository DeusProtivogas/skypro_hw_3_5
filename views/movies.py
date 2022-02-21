from flask import request
from flask_restx import Resource, Namespace

from dao.model.movies import MovieSchema
from service.movies import MovieServices
from implemented import movie_service

movie_ns = Namespace("movies")
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

@movie_ns.route("/")
class MoviesView(Resource):
    def get(self):
        genre = request.args.get("genre_id")
        director = request.args.get("director_id")
        year = request.args.get("year")

        filters = {
            "genre_id": genre,
            "director_id": director,
            "year": year
        }
        all_movies = movie_service.get_all(filters)

        return movies_schema.dump(all_movies), 200


    def post(self):
        req_json = request.json
        # new_film = Movie(**req_json)
        movie = movie_service.create(req_json)
        return movie, 201

@movie_ns.route("/<int:mid>")
class MovieView(Resource):
    def get(self, mid):
        movie = movie_service.get_one(mid)
        return movie_schema.dump(movie), 200

    def put(self, mid):
        data = request.json
        data["id"] = mid
        movie_service.update(data)
        return "", 204

    def delete(self, mid):
        movie_service.delete(mid)
        return "", 204

