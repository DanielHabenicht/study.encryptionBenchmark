from classes import Test


def clear():
    import os
    os.remove("results.md")


def write_file(data):
    f = open("results.md", "w")
    f.write("# Results\n")
    f.write("\n")
    f.close()


def writeTestToFile(test: Test):
    f = open("results.md", "a")
    f.write(f'# {test.name:s}\n')
    f.write(
        f'Key: {test.key:s} ({len(test.key):g})\nNonce: {test.nonce:s}\n\n')
    for testRun in test.testRuns:
        f.write(f'## Filesize: {testRun.fileSize:g}KB\n\n')
        f.write('| Testrun | Encryption (s) | Decryption (s) | Both (s) |\n')
        f.write('|:-------:|:--------------:|:--------------:|:--------:|\n')
        for index, time in enumerate(testRun.times):
            f.write(
                f'| {index+1:g} | {time[0]:0.5f} | {time[1]:0.5f} | {time[2]:0.5f} |\n')

        f.write(
            f'| Median | {testRun.timeEncMedian():0.5f} | {testRun.timeDecMedian():0.5f} | {testRun.timeSumMedian():0.5f} |\n')
        f.write('\n')

    f.write('\n')

    f.close()
