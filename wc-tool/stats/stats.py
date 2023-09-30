from .base import Statistic

class ByteCount(Statistic):
    def process_line(self, line: str):
        _bytes = len(bytes(line, 'utf-8'))
        self.count += _bytes

class WordsCount(Statistic):
    def process_line(self, line: str):
        words = len(line.split())
        self.count += words

class LineCount(Statistic):
    def process_line(self, line: str):
        self.count += 1

class CharCount(Statistic):
    def process_line(self, line: str):
        self.count += len(line)

class FileStatistics:
    def __init__(self):
        self.statistics = []

    def add_statistic(self, statistic):
        self.statistics.append(statistic)

    def process_line(self, line):
        for statistic in self.statistics:
            statistic.process_line(line)

    def get_results(self):
        results = {}
        for statistic in self.statistics:
            results[type(statistic).__name__] = statistic.get_result()
        return results