import statistics


class DataRecord:
    def __init__(self, algorithm: str, times: list):
        self.algorithm = algorithm
        self.times = times

    def timeMedian(self) -> float:
        return statistics.mean(self.times)
