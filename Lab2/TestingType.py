from enum import Enum


class TestingType(Enum):
    TRAIN = 0
    SPLIT = 1
    CROSS = 2

    @staticmethod
    def from_string(string):
        assert type(string) is str

        if string == 'train':
            return TestingType.TRAIN
        elif string == 'split':
            return TestingType.SPLIT
        elif string == 'cross':
            return TestingType.CROSS
