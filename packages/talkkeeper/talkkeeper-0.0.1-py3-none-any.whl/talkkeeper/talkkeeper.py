import hashlib
import io


class Talkkeeper:
    ACCEPTED_FORMATS = [".wav", ".webm"]

    def __init__(self, source):
        self.source = source
        self._content = None

    @property
    def content(self):
        if not self._content:
            if not self.source.exists():
                raise ReadError
            self._content = io.BytesIO(open(self.source, "rb").read()).getvalue()
        return self._content

    @property
    def buffer(self):
        return io.BufferedReader(io.BytesIO(self.content))

    @classmethod
    def get(cls, source):
        # Возвращает список или object класса, если указана папка
        if not source.exists():
            return []
        elif source.is_file():
            yield cls(source)
        elif source.is_dir():
            for file in source.glob("**/*"):
                if file.suffix in cls.ACCEPTED_FORMATS:
                    yield cls(file)

    @property
    def md5(self):
        return hashlib.md5(self.buffer.read()).hexdigest()

    @property
    def map(self):
        # Получение индекса файла
        ...

    @property
    def cursor(self):
        # Токен загрузки
        ...

    def upload(self):
        # Отправить мета информацию, создать/получить курсор загрузки
        # Отправка блоков в загрузку по поличеству ядер - 1
        ...

    def __enter__(self):
        # Проход по файлу
        return self

    def __exit__(self, *args):
        # Закрыть файл
        self.talk.close()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}: {self.source.resolve()}"

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {self.source.resolve()}"


class ReadError(Exception):
    ...
