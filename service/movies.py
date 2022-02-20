from dao.movies import MovieDAO

class MovieServices():
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, bid):
        return self.dao.get_one(bid)

    def get_all(self, filters):
        if filters.get("director_id"):
            return self.dao.get_by_director_id(filters.get("director_id"))
        elif filters.get("genre_id"):
            return self.dao.get_by_genre_id(filters.get("genre_id"))
        elif filters.get("year"):
            return self.dao.get_by_year(filters.get("year"))
        else:
            return self.dao.get_all()

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        self.dao.update(data)
        return self.dao

    def delete(self, mid):
        self.dao.delete(mid)
        return ""

