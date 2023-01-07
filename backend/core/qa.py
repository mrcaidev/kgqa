from .classifier import Classifier
from .database import Database
from .parser import Parser


class QA:
    _BAD_QUESTION_MESSAGE = "抱歉，我无法理解这个问题。请换个问题试试吧！"
    _NOT_FOUND_MESSAGE = "没有找到答案。请换个问题试试吧！"

    def __init__(self):
        self._classifer = Classifier()
        self._database = Database()

    def answer(self, sentence: str):
        print(f"问题：{sentence}")

        label = self._classifer.classify(sentence)
        print(f"类别：{label}")

        parser = Parser(sentence)
        movies = parser.movies
        actors = parser.actors
        genres = parser.genres
        print(f"解析成分：电影={movies}，演员={actors}，类型={genres}")

        try:
            if label == "introduction_by_movie":
                return self._get_introduction_by_movie(movies[0])
            elif label == "rating_by_movie":
                return self._get_rating_by_movie(movies[0])
            elif label == "release_date_by_movie":
                return self._get_release_date_by_movie(movies[0])
            elif label == "actors_by_movie":
                return self._get_actors_by_movie(movies[0])
            elif label == "genres_by_movie":
                return self._get_genres_by_movie(movies[0])
            elif label == "birthday_by_actor":
                return self._get_birthday_by_actor(actors[0])
            elif label == "birthplace_by_actor":
                return self._get_birthplace_by_actor(actors[0])
            elif label == "biography_by_actor":
                return self._get_biography_by_actor(actors[0])
            elif label == "movies_by_actor":
                return self._get_movies_by_actor(actors[0])
            elif label == "movie_num_by_actor":
                return self._get_movie_num_by_actor(actors[0])
            elif label == "actors_by_genre":
                return self._get_actors_by_genre(genres[0])
            elif label == "movies_by_actor_and_genre":
                return self._get_movies_by_actor_and_genre(actors[0], genres[0])
            else:
                return QA._BAD_QUESTION_MESSAGE
        except IndexError:
            return QA._BAD_QUESTION_MESSAGE

    def _get_introduction_by_movie(self, movie_name: str):
        result = self._database.find_one(
            """
            MATCH (m:Movie)
            WHERE m.name = $movie_name
            RETURN m.introduction
            """,
            movie_name=movie_name,
        )
        return result or QA._NOT_FOUND_MESSAGE

    def _get_rating_by_movie(self, movie_name: str):
        result = self._database.find_one(
            """
            MATCH (m:Movie)
            WHERE m.name = $movie_name
            RETURN m.rating
            """,
            movie_name=movie_name,
        )
        return round(result, 1) if result else QA._NOT_FOUND_MESSAGE

    def _get_release_date_by_movie(self, movie_name: str):
        result = self._database.find_one(
            """
            MATCH (m:Movie)
            WHERE m.name = $movie_name
            RETURN m.release_date
            """,
            movie_name=movie_name,
        )
        return result.strftime("%Y/%m/%d") if result else QA._NOT_FOUND_MESSAGE

    def _get_actors_by_movie(self, movie_name: str):
        results = self._database.find_many(
            """
            MATCH (a:Actor)-[STARS_IN]->(m:Movie)
            WHERE m.name = $movie_name
            RETURN a.name
            """,
            movie_name=movie_name,
        )
        return "、".join(results) if results else QA._NOT_FOUND_MESSAGE

    def _get_genres_by_movie(self, movie_name: str):
        results = self._database.find_many(
            """
            MATCH (m:Movie)-[BELONGS_TO]->(g:Genre)
            WHERE m.name = $movie_name
            RETURN g.name
            """,
            movie_name=movie_name,
        )
        return "、".join(results) if results else QA._NOT_FOUND_MESSAGE

    def _get_birthday_by_actor(self, actor_name: str):
        result = self._database.find_one(
            """
            MATCH (a:Actor)
            WHERE a.name = $actor_name
            RETURN a.birthday
            """,
            actor_name=actor_name,
        )
        return result or QA._NOT_FOUND_MESSAGE

    def _get_birthplace_by_actor(self, actor_name: str):
        result = self._database.find_one(
            """
            MATCH (a:Actor)
            WHERE a.name = $actor_name
            RETURN a.birthplace
            """,
            actor_name=actor_name,
        )
        return result or QA._NOT_FOUND_MESSAGE

    def _get_biography_by_actor(self, actor_name: str):
        result = self._database.find_one(
            """
            MATCH (a:Actor)
            WHERE a.name = $actor_name
            RETURN a.biography
            """,
            actor_name=actor_name,
        )
        return result or QA._NOT_FOUND_MESSAGE

    def _get_movies_by_actor(self, actor_name: str):
        results = self._database.find_many(
            """
            MATCH (a:Actor)-[STARS_IN]->(m:Movie)
            WHERE a.name = $actor_name
            RETURN m.name
            """,
            actor_name=actor_name,
        )
        return "、".join(results) if results else QA._NOT_FOUND_MESSAGE

    def _get_movie_num_by_actor(self, actor_name: str):
        result = self._database.find_one(
            """
            MATCH (a:Actor)-[STARS_IN]->(m:Movie)
            WHERE a.name = $actor_name
            RETURN COUNT(m)
            """,
            actor_name=actor_name,
        )
        return result or QA._NOT_FOUND_MESSAGE

    def _get_genres_by_actor(self, actor_name: str):
        results = self._database.find_many(
            """
            MATCH (a:Actor)-[STARS_IN]->(Movie)-[BELONGS_TO]->(g:Genre)
            WHERE a.name = $actor_name
            RETURN DISTINCT g.name
            """,
            actor_name=actor_name,
        )
        return "、".join(results) if results else QA._NOT_FOUND_MESSAGE

    def _get_movies_by_actor_and_genre(self, actor_name: str, genre_name: str):
        results = self._database.find_many(
            """
            MATCH (a:Actor)-[STARS_IN]->(m:Movie)-[BELONGS_TO]->(g:Genre)
            WHERE a.name = $actor_name AND g.name = $genre_name
            RETURN m.name
            """,
            actor_name=actor_name,
            genre_name=genre_name,
        )
        return "、".join(results) if results else QA._NOT_FOUND_MESSAGE


if __name__ == "__main__":
    import dotenv

    dotenv.load_dotenv()

    qa = QA()
    while True:
        sentence = input("请输入问题：")
        print(qa.answer(sentence))
