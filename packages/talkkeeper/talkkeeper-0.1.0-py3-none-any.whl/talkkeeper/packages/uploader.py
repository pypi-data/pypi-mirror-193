from talkkeeper import talkkeeper
from talkkeeper.packages.index import Index


class Uploader:
    def __init__(self, path):
        self.path = path
        self.index = Index()
        self.__iterator = None

    def __iter__(self):
        self.__iterator = iter(self.get(self.path))
        return self

    def __next__(self):
        return next(self.__iterator)

    @property
    def cursor(self):
        # Токен загрузки
        ...

    def upload(self):
        # Отправить мета информацию, создать/получить курсор загрузки
        # Отправка блоков в загрузку по поличеству ядер - 1
        ...

    @classmethod
    def get(cls, source):
        # Возвращает список или object класса, если указана папка
        if not source.exists():
            return []
        elif source.is_file():
            yield talkkeeper.Talkkeeper(source)
        elif source.is_dir():
            for file in source.glob("**/*"):
                try:
                    tk = talkkeeper.Talkkeeper(file)
                except talkkeeper.ReadError:
                    continue
                else:
                    yield tk
