class Rating:

    def __init__(self,  user_id: int, movie_id: int, rating: int, timestamp: str) -> None:
        self.user_id = user_id
        self.movie = movie_id
        self.rating = rating
        self.timestamp = timestamp
