from flask_restful import Resource

from model.tag import Tag
from utils import get_rows_from_csv


class TagView(Resource):

    def get(self):
        tag_rows = get_rows_from_csv('./static/tags.csv')
        return [Tag(row[0], row[1], row[2], row[3]).__dict__ for row in tag_rows]
