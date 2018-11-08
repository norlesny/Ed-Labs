from Lab2.solver.Metric import Metric


class DataEntry:

    def __init__(self, attributes, classification=0) -> None:
        assert type(attributes) is list

        self.attributes = attributes
        self.classification = classification

    def distance(self, other, metric=Metric.EUCLIDES):
        assert type(other) is DataEntry
        assert type(metric) is Metric

        zipped_attributes = zip(self.attributes, other.attributes)
        if metric == Metric.EUCLIDES:
            return DataEntry._euclides_distance(zipped_attributes)
        elif metric == Metric.MANHATTAN:
            return DataEntry._manhattan_distance(zipped_attributes)
        else:
            print("Unknown metric selected: {metric}")

    @staticmethod
    def _euclides_distance(zipped_attributes):
        sum = 0
        for x, y in zipped_attributes:
            sum += (x - y) ** 2

        return sum ** 0.5

    @staticmethod
    def _manhattan_distance(zipped_attributes):
        sum = 0
        for x, y in zipped_attributes:
            sum += abs(x - y)

        return sum
