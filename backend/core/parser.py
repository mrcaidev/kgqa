import os

import jieba
import jieba.posseg as jp

USERDICT_PATH = os.path.join("data", "userdict.txt")

jieba.setLogLevel("ERROR")
jieba.load_userdict(USERDICT_PATH)


class Parser:
    """
    语句解析器。

    从语句中解析出演员、电影和类型。
    """

    def __init__(self, sentence: str):
        self._pairs = jp.lcut(sentence)

    def _get_words_by_flag(self, flag: str):
        return [pair.word for pair in self._pairs if pair.flag == flag]

    @property
    def actors(self):
        return self._get_words_by_flag("nr")

    @property
    def movies(self):
        return self._get_words_by_flag("nm")

    @property
    def genres(self):
        return self._get_words_by_flag("ng")


if __name__ == "__main__":
    while True:
        sentence = input("请输入语句：").strip()
        parser = Parser(sentence)
        print(f"解析成分：演员={parser.actors}，电影={parser.movies}，类型={parser.genres}")
