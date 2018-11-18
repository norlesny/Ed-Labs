from enum import Enum


class Metric(Enum):
    EUCLIDES = 0
    MANHATTAN = 1

    @staticmethod
    def from_str(string):
        assert type(string) is str

        if string == 'euclides':
            return Metric.EUCLIDES
        elif string == 'manhattan':
            return Metric.MANHATTAN
