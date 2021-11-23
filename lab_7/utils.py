import csv

from model.movie import Movie


def get_all_movies() -> list[Movie]:
    with open('./static/movies.csv', newline='', encoding="utf8") as csvf:
        reader = csv.DictReader(csvf)
        return [Movie(row['movieId'], row['title'], row['genres'])
                for row in reader]
