
from Cryptodome.Cipher import AES
from Cryptodome import Random
import base64


def encrypt(key: str, raw: str) -> bytes:
    # encrypt a given string. returns a base64 encoded bytes object
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CTR, iv)
    return base64.b64encode(iv + cipher.encrypt(raw.encode("utf-8")))


def decrypt(key: str, enc: bytes) -> str:
    # decrypt a given base64 bytes object. returns a string
    enc = base64.b64decode(enc)
    iv = enc[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CTR, iv)
    return cipher.decrypt(enc[AES.block_size:]).decode("utf-8")
