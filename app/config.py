import os
from dotenv import load_dotenv


class Settings():
    BOT_TOKEN: str = ''
    BASE_SITE: str = ''
    ADMIN_ID: int = 0
    ZULIP_API_KEY: str = ''
    ZULIP_EMAIL: str = ''
    ZULIP_SITE: str = ''
    ZULIP_ALLOW_INSECURE: bool = False
    ZULIP_STAFF_IDS: list = []

    def __init__(self, env_file=''):
        load_dotenv()

        for attr_name in dir(Settings):
            if not attr_name.isupper():
                continue

            attr_val = getattr(Settings, attr_name)
            env_val = self._get_env_val(attr_name)

            if isinstance(attr_val, bool):
                setattr(Settings, attr_name, self._str2bool(env_val))
            elif isinstance(attr_val, int):
                setattr(Settings, attr_name, int(env_val))   # если не int - будет ValueError
            elif isinstance(attr_val, list):
                setattr(Settings, attr_name, env_val.split(','))
            else:
                setattr(Settings, attr_name, env_val)

            # debug
            # attr_val = getattr(Settings, attr_name)
            # print(attr_name, ': ', attr_val)

    def _get_env_val(self, attr_name):
        val = os.getenv(attr_name)
        if val is None:
            raise NameError(f'No {attr_name} setting in .env')

        return val

    def _str2bool(self, str_bool: str):
        if str_bool.lower() in ('1', 'yes', 'true', 'on'):
            return True
        elif str_bool.lower() in ('0', 'no', 'false', 'off'):
            return False
        else:
            raise ValueError(f'Invalid value for BOOL - {str_bool}.')

settings = Settings()


if __name__ == "__main__":
    settings = Settings()
