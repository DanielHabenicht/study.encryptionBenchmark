
from Cryptodome.Cipher import AES
from Cryptodome import Random
from Cryptodome.Random import get_random_bytes
import base64


def encrypt(key: str, raw: str) -> bytes:
    # encrypt a given string. returns a base64 encoded bytes object
    # iv = Random.new().read(16)
    cipher = AES.new(key, AES.MODE_CTR)
    cipherText = cipher.encrypt(raw.encode("utf-8"))
    return base64.b64encode(cipher.nonce + cipherText)


def decrypt(key: str, enc: bytes) -> str:
    # decrypt a given base64 bytes object. returns a string
    enc = base64.b64decode(enc)
    nonce = enc[:8]
    cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
    return cipher.decrypt(enc[8:]).decode("utf-8")
