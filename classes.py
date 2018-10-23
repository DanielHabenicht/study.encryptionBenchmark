

class Test:
    def __init__(self, name: str, algorithm, key: str, nonce: str, testRuns: list):
        self.name = name
        self.nonce = nonce
        self.algorithm = algorithm
        self.key = key
        self.testRuns = testRuns


class TestRun:
    def __init__(self, fileSize: int, times: list):
        self.fileSize = fileSize
        # self.iteration = iteration
        # times is a list of tupel of (encryption, decryption, whole)
        self.times = times

    def timeEncMedian(self) -> float:
        import statistics
        return statistics.mean([i[0] for i in self.times])

    def timeDecMedian(self) -> float:
        import statistics
        return statistics.mean([i[1] for i in self.times])

    def timeSumMedian(self) -> float:
        import statistics
        return statistics.mean([i[2] for i in self.times])
