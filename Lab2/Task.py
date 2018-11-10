import argparse
import sys

sys.path.append('../')

from Lab2.solver import CsvDataParser
from Lab2.solver.Metric import Metric
from Lab2.solver.KNNSolver import KNNSolver

parser = argparse.ArgumentParser(description="k-NN algorithm")

parser.add_argument('data_file', type=str, help='path of the file with the data set')
parser.add_argument('-k', type=int, default=5, help='the value of k in the algorithm')
parser.add_argument('-m', type=str, default='euclides', choices=['euclides', 'manhattan'],
                    help='the metric to be used')
parser.add_argument('-d', type=int, default=-1, help='the index of the classification attribute')

args = parser.parse_args()

solver = KNNSolver(int(args.__getattribute__('k')), Metric.from_str(args.__getattribute__('m')))

data_set = CsvDataParser.read_data(args.__getattribute__('data_file'))
solver.set_learning_data(data_set)

result = solver.classify(data_set[100])
print(result)

print("Finished")
