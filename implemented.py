# файл для создания DAO и сервисов чтобы импортировать их везде

# book_dao = BookDAO(db.session)
# book_service = BookService(dao=book_dao)
#
# review_dao = ReviewDAO(db.session)
# review_service = ReviewService(dao=review_dao)
from dao.directors import DirectorDAO
from dao.genres import GenreDAO
from dao.movies import MovieDAO
from service.directors import DirectorServices
from service.genres import GenreServices
from service.movies import MovieServices
from setup_db import db

movie_dao = MovieDAO(db.session)
movie_service = MovieServices(dao=movie_dao)


director_dao = DirectorDAO(db.session)
director_service = DirectorServices(dao=director_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreServices(dao=genre_dao)
