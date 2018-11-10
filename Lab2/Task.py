from Lab2.solver import CsvDataParser
from Lab2.solver.DataEntry import DataEntry
from Lab2.solver.KNNSolver import KNNSolver
from Lab2.solver.Metric import Metric

solver = KNNSolver(5, Metric.MANHATTAN)

test_data = DataEntry([13.5,3.12,2.62,24,123,1.4,1.57,.22,1.25,8.60,.59,1.3,500])

data_set = CsvDataParser.read_data("wine.data", 0)
solver.set_learning_data(data_set)
result = solver.classify(test_data)

print(str(result))

print("Finished")
