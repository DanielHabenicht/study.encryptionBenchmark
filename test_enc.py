import time
import encryption
from classes import Test, TestRun
import os

filesFolder = "files"


def testEncrypt(test: Test, files: list, iterations: int) -> Test:
    print(f'Start test for {test.name:s}:')
    for fileSize in files:
        f = open(filesFolder + f'/{fileSize:g}MB.dat')
        testString = f.read()
        f.close()
        print(f'   Test with {fileSize:g}MB File')
        times = []

        for i in range(iterations):
            print(f'    - Iteration {i:g}')

            start = time.time()
            cipherText = test.algorithm.encrypt(
                test.key.encode("utf-8"), testString)

            decrypt = time.time()

            # In Memory Encryptio and Decryption
            test.algorithm.decrypt(test.key.encode("utf-8"), cipherText)

            #     print('Something is wrong!')
            # Test if encryption and decryption works
            # if not test.algorithm.decrypt(test.key, test.algorithm.encrypt(test.key, testString)) == testString:
            #     print('Something is wrong!')
            times.append((decrypt-start,
                          time.time()-decrypt,
                          time.time()-start))

        size = os.path.getsize(filesFolder + f'/{fileSize:g}MB.dat') >> 10
        test.testRuns.append(TestRun(size, times))

    return test
