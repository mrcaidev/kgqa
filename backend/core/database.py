import os

from neo4j import GraphDatabase


class Database:
    """
    Neo4j 数据库访问层。

    管理数据库连接的生命周期，并提供查询接口。
    """

    def __init__(self):
        uri = os.environ["DATABASE_URI"]
        user = os.environ["DATABASE_USER"]
        password = os.environ["DATABASE_PASSWORD"]

        try:
            self._driver = GraphDatabase.driver(uri, auth=(user, password))
            self._session = self._driver.session()
        except Exception as e:
            raise Exception("数据库连接失败") from e

    def close(self):
        try:
            self._session.close()
            self._driver.close()
        except Exception as e:
            raise Exception("数据库断开失败") from e

    def find_one(self, query: str, **parameters):
        result = self._session.run(query, parameters).single()
        return result.value() if result else None

    def find_many(self, query: str, **parameters):
        return self._session.run(query, parameters).value()


if __name__ == "__main__":
    import dotenv

    dotenv.load_dotenv()

    database = Database()
    genres = database.find_many(
        """
        MATCH (m:Movie)-[BELONGS_TO]->(g:Genre)
        WHERE m.name = $movie_name
        RETURN g.name
        """,
        movie_name="卧虎藏龙",
    )
    database.close()

    print(genres)
