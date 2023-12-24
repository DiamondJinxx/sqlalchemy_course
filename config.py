from pydantic_settings import BaseSettings, SettingsConfigDict

ENV_FILES = ("dev.env",)


class DBConfig(BaseSettings):
    """Database settings"""
    USER: str
    PASSWORD: str
    HOST: str
    PORT: int
    DB_NAME: str

    model_config = SettingsConfigDict(
        case_sensitive=True,
        env_file=ENV_FILES,
        env_prefix="DATABASE_"
    )

    @property
    def url_psycopg(self):
        return f"postgresql+psycopg://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DB_NAME}"

    @property
    def url_asyncpg(self):
        return f"postgresql+asyncpg://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DB_NAME}"


db_settings = DBConfig()
