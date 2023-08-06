from core.conf.base_settings import BaseConfig


class Seetings(BaseConfig):
    DEBUG = True

    # Choose a Password Hasher Default is bcrypt
    # "sha256_crypt", "md5_crypt", "bcrypt", "pbkdf2_sha256","pbkdf2_sha512"
    PASSWORD_HASHER = "bcrypt"

    DATABASE_URL = ""


settings = Seetings()
