class Movie:

    def __init__(self, movie_id: int, title: str, genres: str) -> None:
        self._movie = movie_id
        self._title = title
        self._genres = genres
