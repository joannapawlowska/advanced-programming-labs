from flask import Flask
from flask_restful import Api


from view.movie_view import MovieView

app = Flask(__name__)
api = Api(app)

api.add_resource(MovieView, '/api/movies')

if __name__ == '__main__':
    app.run(debug=True)
