from Lab2.solver.DataEntry import DataEntry
from Lab2.solver.KNNSolver import KNNSolver
from Lab2.solver.Metric import Metric

solver = KNNSolver(5, Metric.MANHATTAN)

a = [
    DataEntry([1, 5], 0),
    DataEntry([2, 6], 0),
    DataEntry([2, 7], 1),
    DataEntry([3, 7], 0),
    DataEntry([3, 8], 1),
    DataEntry([4, 8], 0),
    DataEntry([5, 1], 1),
    DataEntry([5, 9], 0),
    DataEntry([6, 2], 1),
    DataEntry([7, 2], 0),
    DataEntry([7, 3], 1),
    DataEntry([8, 3], 0),
    DataEntry([8, 4], 1),
    DataEntry([9, 5], 1),
    DataEntry([10, 6], 1)]

b = DataEntry([5, 5])

solver.set_learning_data(a)
result = solver.classify(b)

print(str(result))

print("Finished")
