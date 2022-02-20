from dao.model.directors import Director

class DirectorDAO():
    def __init__(self, session):
        self.session = session

    def get_one(self, did):
        return self.session.query(Director).get(did)

    def get_all(self):
        return self.session.query(Director).all()

    def get_by_director_id(self, did):
        return self.session.query(Director).filter(Director.id == did).all()

    def create(self, data):
        new_director = Director(**data)
        self.session.add(new_director)
        self.session.commit()
        return new_director

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
