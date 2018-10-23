import test_enc
import time
import generateFiles
import out_file
from encryption import des3, des, AEScbc, AESctr, AESecb, rc4
from classes import Test
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import DES3
from generateFiles import generateRandomString


desKey = generateRandomString(8)
key128bit = generateRandomString(16)

while True:
    try:
        des3parityKey = DES3.adjust_key_parity(
            generateRandomString(16).encode("utf-8")).decode("utf-8")
        break
    except ValueError:
        pass

print('Setting up Test')
out_file.clear()

algorithms = [
    Test("DES", des, desKey, "none", []),
    Test("DES3", des3, des3parityKey, "none", []),
    Test("AES_CBC", AEScbc, key128bit, "none", []),
    Test("AES_CTR", AESctr, key128bit, "none", []),
    Test("AES_ECB", AESecb, key128bit, "none", []),
    Test("RC4", rc4, key128bit, "none", [])
]
filesSizes = [1, 10, 100]
iterations = 20
generateFiles.gen(filesSizes)


for index, testCase in enumerate(algorithms):
    doneTestCase = test_enc.testEncrypt(testCase, filesSizes, iterations)
    print(
        f'{doneTestCase.testRuns[0].timeSumMedian():.5f} seconds')
    out_file.writeTestToFile(doneTestCase)
    algorithms[index] = doneTestCase

out_file.writeSummary(algorithms)

print('Wrote results to "./results.md"!')
