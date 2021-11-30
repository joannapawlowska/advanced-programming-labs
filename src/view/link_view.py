from flask_restful import Resource

from src.model.link import Link
from src.utils import get_rows_from_csv


class LinkView(Resource):

    def get(self):
        link_rows = get_rows_from_csv('./src/static/links.csv')
        return [Link(row[0], row[1], row[2]).__dict__ for row in link_rows]
