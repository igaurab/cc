from abc import ABC, abstractmethod

class Statistic(ABC):
    def __init__(self, enabled=False) -> None:
        self.enable = enabled
        self.count = 0
    
    @abstractmethod
    def process_line(self, line: str) -> None:
        pass

    def get_result(self):
        return self.count