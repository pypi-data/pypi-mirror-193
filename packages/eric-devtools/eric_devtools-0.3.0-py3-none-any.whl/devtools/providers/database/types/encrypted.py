from sqlalchemy import Text
from sqlalchemy.engine import Dialect
from sqlalchemy.types import TypeDecorator

from devtools.providers.crypto import CryptoProvider


class EncryptedString(TypeDecorator):

    impl = Text

    cache_ok = True

    def __init__(
        self, crypto_provider: CryptoProvider | None = None, *args, **kwargs
    ) -> None:
        self.crypto_provider = crypto_provider or CryptoProvider()
        super().__init__(*args, **kwargs)

    def process_bind_param(self, value: str | None, dialect: Dialect):
        del dialect
        return value and self.crypto_provider.encrypt(value)

    def process_result_value(self, value: str | None, dialect: Dialect):
        del dialect
        return value and self.crypto_provider.decrypt(value)
