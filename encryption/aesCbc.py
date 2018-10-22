
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
import base64
import json
from Cryptodome import Random


def encrypt(self, raw: str) -> bytes:
    """ encrypt a given string. returns a base64 encoded bytes object """

    raw = self._pad(raw)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(self.key, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(raw.encode("utf-8")))


def decrypt(self, enc: bytes) -> str:
    """ decrypt a given base64 bytes object. returns a string """
    enc = base64.b64decode(enc)
    iv = enc[:AES.block_size]
    cipher = AES.new(self.key, AES.MODE_CBC, iv)
    return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode("utf-8")
