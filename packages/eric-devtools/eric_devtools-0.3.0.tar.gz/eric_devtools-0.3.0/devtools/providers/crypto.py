import codecs
from base64 import b64decode
from secrets import token_urlsafe

from cffi.backend_ctypes import long
from Crypto.Cipher import AES
from Crypto.Util import Counter

from devtools import config as tk_config
from devtools.providers.config import ProviderConfig, from_env
from devtools.utils import helpers


class CryptoConfig(ProviderConfig):
    _prefix_ = 'crypto'

    iv: str
    key: str

    @property
    def bytes_iv(self):
        return self.iv.encode()[:16]

    @property
    def bytes_key(self):
        return self.key.encode()[:32]


class CryptoProvider:
    def __init__(
        self, config: CryptoConfig | None = None, byte_size: int = 128,
    ):
        self._config = config or from_env(CryptoConfig)
        self._byte_size = byte_size

    @classmethod
    def to_test(cls):
        return cls(CryptoConfig(iv=token_urlsafe(), key=token_urlsafe()))

    @classmethod
    @helpers.deprecated
    def from_env(cls, config: tk_config.ConfigLike = tk_config.Config()):
        return cls(from_env(CryptoConfig, config=config))

    def _get_aes_driver(self, byte_size: int):
        counter = Counter.new(
            byte_size,
            initial_value=long(
                codecs.encode(obj=self.config.bytes_iv, encoding='hex_codec'),
                16,
            ),
        )
        return AES.new(self.config.bytes_key, AES.MODE_CTR, counter=counter)

    @property
    def _driver(self):
        return self._get_aes_driver(self._byte_size)

    @property
    def config(self):
        return self._config

    def encrypt(self, value: str) -> str:
        return helpers.encode_base_64(
            self._driver.encrypt(value.encode(helpers.DEFAULT_ENCODING))
        ).decode()

    def decrypt(self, value: str) -> str:
        if not value:
            return value
        if not helpers.is_base_64(value):
            return value
        decrypted_value = self._driver.decrypt(b64decode(value))
        return decrypted_value.decode(helpers.DEFAULT_ENCODING)
