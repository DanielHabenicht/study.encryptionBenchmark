import random
import string
import os

seed = "ThatsAGreatSeed"
filesFolder = "files"


def gen(files: list):
    print(f'Generating test files under ./{filesFolder}:')
    # Ensure path exists
    if not os.path.exists(filesFolder):
        os.makedirs(filesFolder)

    for i in files:
        if os.path.isfile(filesFolder + f'/{i:g}MB.dat'):
            print(f' - File "{i:g}MB.dat" already exists')
        else:
            print(f' - Generating "{i:g}MB.dat" File...')
            generateFile(i, filesFolder)

    print('Generated all Files.')


def generateFile(sizeInMB: int, path: str):
    file = open(path + f'/{sizeInMB:g}MB.dat', "w")

    file.write(generateRandomString(sizeInMB, seed))

    file.close()


# size in MB
def generateRandomString(size, seed=None):
    if seed != None:
        random.seed(seed)
    return(''.join(random.choice(string.ascii_letters) for i in range(size * pow(2, 20))))


def pow(x: int, y: int) -> int:
    if (y == 0):
        return 1
    elif (int(y % 2) == 0):
        return (pow(x, int(y / 2)) *
                pow(x, int(y / 2)))
    else:
        return (x * pow(x, int(y / 2)) *
                pow(x, int(y / 2)))
