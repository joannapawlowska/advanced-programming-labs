from flask_restful import Resource

from src.model.movie import Movie
from src.utils import get_rows_from_csv


class MovieView(Resource):

    def get(self):
        movie_rows = get_rows_from_csv('./src/static/movies.csv')
        return [Movie(row[0], row[1], row[2]).__dict__ for row in movie_rows]
