from Cryptodome.Cipher import ARC4
from Cryptodome.Hash import SHA
from Cryptodome.Random import get_random_bytes
from Cryptodome import Random
import base64


def encrypt(key: str, raw: str) -> bytes:
    # encrypt a given string. returns a base64 encoded bytes object
    nonce = get_random_bytes(16)
    tempkey = SHA.new(key+nonce).digest()
    cipher = ARC4.new(tempkey)
    return base64.b64encode(nonce + cipher.encrypt(raw.encode("utf-8")))


def decrypt(key: str, enc: bytes) -> str:
    # decrypt a given base64 bytes object. returns a string
    enc = base64.b64decode(enc)
    nonce = enc[:16]
    tempkey = SHA.new(key+nonce).digest()
    cipher = ARC4.new(tempkey)
    return cipher.decrypt(enc[16:]).decode("utf-8")
