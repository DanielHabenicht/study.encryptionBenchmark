from Cryptodome.Cipher import DES
from Cryptodome import Random
import base64


def encrypt(key: str, raw: str) -> bytes:
    # encrypt a given string. returns a base64 encoded bytes object
    iv = Random.new().read(DES.block_size)
    cipher = DES.new(key, DES.MODE_OFB, iv)
    return base64.b64encode(iv + cipher.encrypt(raw.encode("utf-8")))


def decrypt(key: str, enc: bytes) -> str:
    # decrypt a given base64 bytes object. returns a string
    enc = base64.b64decode(enc)
    iv = enc[:DES.block_size]
    cipher = DES.new(key, DES.MODE_OFB, iv)
    return cipher.decrypt(enc[DES.block_size:]).decode("utf-8")
