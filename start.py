import test_enc
import time
import generateFiles
import out_file
from encryption import des3, des, AEScbc, AESctr, AESecb, rc4

filesSizes = [1, 10, 100]

print('Setting up Test')
generateFiles.gen(filesSizes)

algorithms = [
    ("DES", des),
    ("DES3", des3),
    ("AES_CBC", AEScbc),
    ("AES_CTR", AESctr),
    ("AES_ECB", AESecb),
    ("RC4", rc4)
]

for alg in algorithms:
    times = test_enc.testEncrypt("test", filesSizes, alg)
    print(f'{times.times[1]-times.times[0]:.5f} seconds')


matrix = [
    [0,   0.1,      "hoge", True,   0,      "2017-01-01 03:04:05+0900"],
    [2,   "-2.23",  "foo",  False,  None,   "2017-12-23 45:01:23+0900"],
    [3,   0,        "bar",  "true",  "inf", "2017-03-03 33:44:55+0900"],
    [-10, -9.9,     "",     "FALSE", "nan", "2017-01-01 00:00:00+0900"],
]

out_file.write_file(matrix)

# print(f'{times[1]-times[0]:.5f} seconds')
