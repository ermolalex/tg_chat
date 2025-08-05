import os
from dotenv import load_dotenv


class Settings():
    BOT_TOKEN = ''
    BASE_SITE = ''
    ERR = ''

    def __init__(self, env_file=''):
        load_dotenv()

        for attr_name in dir(Settings):
            if attr_name.isupper():
                print(attr_name)
                setattr(Settings, attr_name, self._get_env_val(attr_name))

    def _get_env_val(self, attr_name):
        val = os.getenv(attr_name)
        assert val is not None, f'No {attr_name} setting in .env'

        return val

if __name__ == "__main__":
    settings = Settings()
    print(settings.BOT_TOKEN, settings.ERR)

# Access the string variable
# my_list_str = os.getenv('MY_LIST')

"""
from pydantic_settings import BaseSettings, SettingsConfigDict

class _Settings(BaseSettings):
    BOT_TOKEN: str
    BASE_SITE: str
    ADMIN_ID: int
    ZULIP_API_KEY: str
    ZULIP_EMAIL: str
    ZULIP_SITE: str
    ZULIP_ALLOW_INSECURE: bool
    ZULIP_STAFF_IDS: list[int]

    RABBIT_USER: str
    RABBIT_USER_PSW: str

    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".env")
    )

    def get_webhook_url(self) -> str:
        # Возвращает URL вебхука с кодированием специальных символов.
        return f"{self.BASE_SITE}/webhook"


settings = Settings()
"""