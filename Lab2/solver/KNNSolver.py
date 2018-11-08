from Lab2.solver.Metric import Metric


class KNNSolver:

    def __init__(self, k, metric) -> None:
        assert type(k) is int
        assert type(metric) is Metric
        self._learning_data = []
        self._k = k
        self._metric = metric

    def set_learning_data(self, learning_data):
        self._learning_data = learning_data

    def classify(self, data):
        #  1. obliczyć odległości pomiędzy learning_data a data
        #  2. posortować odległości
        #  3. wybrać k elementów z posortowanej liczby
        #  4. znaleźć najczęstszy wynik z wybranych elementów (jeśli remis -> losowy)
        pass
