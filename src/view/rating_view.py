from flask_restful import Resource

from src.model.rating import Rating
from src.utils import get_rows_from_csv


class RatingView(Resource):

    def get(self):
        rating_rows = get_rows_from_csv('./src/static/ratings.csv')
        return [Rating(row[0], row[1], row[2], row[3]).__dict__ for row in rating_rows]