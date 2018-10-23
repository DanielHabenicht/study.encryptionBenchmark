import time
import encryption
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import DES3
import classes


# 128 Bit Key


def testEncrypt(type: str, files: list, algTupel: tuple) -> classes.DataRecord:
    fh = open("files/10MB.dat", "r")
    testString = fh.read()
    # testString = "This is a test String Everything"
    fh.close()
    algorithm = algTupel[1]
    if algTupel[0] == "DES":
        key = get_random_bytes(8)
    elif algTupel[0] == "DES3":
        while True:
            try:
                key = DES3.adjust_key_parity(get_random_bytes(16))
                break
            except ValueError:
                pass
    else:
        key = get_random_bytes(16)

    print(f'Start test for {algTupel[0]:s}:')
    start = time.time()

    if not algorithm.decrypt(key, algorithm.encrypt(key, testString)) == testString:
        print('Something is wrong!')

    return classes.DataRecord("", [start, time.time()])
