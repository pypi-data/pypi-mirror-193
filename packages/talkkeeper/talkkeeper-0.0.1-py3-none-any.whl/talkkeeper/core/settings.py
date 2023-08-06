from pydantic import BaseSettings


class CoreSettings(BaseSettings):
    ...


class S3Settings(BaseSettings):
    ENDPOINT_URL: str = "https://storage.yandexcloud.net"
    BUCKET_NAME: str = "talkkeeper"
    ACCESS_KEY: str
    SECRET_KEY: str
