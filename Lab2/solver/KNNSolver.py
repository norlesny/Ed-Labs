from Lab2.solver.DataEntry import DataEntry
from Lab2.solver.Metric import Metric


class KNNSolver:

    def __init__(self, k, metric) -> None:
        assert type(k) is int
        assert type(metric) is Metric

        self._learning_data = []
        self._k = k
        self._metric = metric

    def set_learning_data(self, learning_data):
        assert type(learning_data) is list
        for entry in learning_data:
            assert type(entry) is DataEntry

        self._learning_data = learning_data

    @staticmethod
    def take_second(element):
        return element[1]

    def classify(self, data):
        assert type(data) is DataEntry

        #  1. obliczyć odległości pomiędzy learning_data a data
        distances_map = []
        for entry in self._learning_data:
            distances_map.append([entry.classification, data.distance(entry, self._metric)])

        #  2. posortować odległości
        distances_map.sort(key=KNNSolver.take_second)

        #  3. wybrać k elementów z posortowanej liczby
        classifications = {}
        for entry in distances_map[:self._k]:
            classification = str(entry[0])
            if classification in classifications:
                classifications[classification] += 1
            else:
                classifications[classification] = 1

        # 4. znaleźć najczęstszy wynik z wybranych elementów (jeśli remis -> losowy)
        return max(classifications, key=classifications.get)
