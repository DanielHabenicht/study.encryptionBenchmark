import time
from encryption import AEScbc
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import DES3


# 128 Bit Key
key = get_random_bytes(16)
while True:
    try:
        key = DES3.adjust_key_parity(get_random_bytes(16))
        break
    except ValueError:
        pass


def testEncrypt(type: str, files: list) -> [time, time]:
    fh = open("./files/100MB.dat", "r")
    testString = fh.read()
    fh.close()

    start = time.time()

    AEScbc.decrypt(key, AEScbc.encrypt(key, testString))

    return [start, time.time()]
