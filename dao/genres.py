from dao.model.genres import Genre

class GenreDAO():
    def __init__(self, session):
        self.session = session

    def get_one(self, gid):
        return self.session.query(Genre).get(gid)

    def get_all(self):
        return self.session.query(Genre).all()

    def get_by_genre_id(self, did):
        return self.session.query(Genre).filter(Genre.id == did).all()

    def create(self, data):
        new_genre = Genre(**data)
        self.session.add(new_genre)
        self.session.commit()
        return new_genre

    # def delete(self, gid):
    #     genre = self.session.query(Genre).get(gid)
    #
    #     self.session.delete(genre)
    #     self.session.commit()
    #
    #     return genre

    # def update(self, data):
    #     gid = data.get("id")
    #
    #     genre = self.session.query(Genre).get(gid)
    #
    #     genre.name = data.get("name")
    #
    #     self.session.add(genre)
    #     self.session.commit()
    #
    #     return genre
