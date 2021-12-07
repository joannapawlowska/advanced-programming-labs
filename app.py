from flask import Flask
from flask_restful import Api

from src.view.movie_view import MovieView
from src.view.rating_view import RatingView
from src.view.tag_view import TagView
from src.view.link_view import LinkView

app = Flask(__name__)
api = Api(app)

api.add_resource(MovieView, '/api/movies')
api.add_resource(RatingView, '/api/ratings')
api.add_resource(TagView, '/api/tags')
api.add_resource(LinkView, '/api/links')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
