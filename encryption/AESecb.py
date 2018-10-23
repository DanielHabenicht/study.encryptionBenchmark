
from Cryptodome.Cipher import AES
import base64


def encrypt(key: str, raw: str) -> bytes:
    # encrypt a given string. returns a base64 encoded bytes object
    cipher = AES.new(key, AES.MODE_ECB)
    return base64.b64encode(cipher.encrypt(raw.encode("utf-8")))


def decrypt(key: str, enc: bytes) -> str:
    # decrypt a given base64 bytes object. returns a string
    enc = base64.b64decode(enc)
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(enc).decode("utf-8")
