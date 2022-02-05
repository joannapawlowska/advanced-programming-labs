from flask_restful import Resource
from utils import get_all_movies


class MovieView(Resource):

    def get(self):
        return [movie.__dict__ for movie in get_all_movies()]
