import argparse
import sys

sys.path.append('../')

from Lab2.solver import CsvDataParser
from Lab2.solver.KNNSolver import KNNSolver
from Lab2.solver.Metric import Metric
from Lab2.TestingType import TestingType

parser = argparse.ArgumentParser(description="k-NN algorithm")

parser.add_argument('data_file', type=str, help='path of the file with the data set')
parser.add_argument('-k', type=int, default=5, help='the value of k in the algorithm')
parser.add_argument('-m', type=str, default='euclides', choices=['euclides', 'manhattan'],
                    help='the metric to be used')
parser.add_argument('-d', type=int, default=-1, help='the index of the classification attribute')
parser.add_argument('-t', type=str, default='train', choices=['train', 'split', 'cross'],
                    help='how the testing data set will be chosen')

args = parser.parse_args()

solver = KNNSolver(int(args.__getattribute__('k')), Metric.from_str(args.__getattribute__('m')))
data_set = CsvDataParser.read_data(args.__getattribute__('data_file'))

testing_type = TestingType.from_string(args.__getattribute__('t'))
if testing_type == TestingType.TRAIN:
    correct_count = 0
    solver.set_learning_data(data_set)
    print('class\t\tdata')
    for entry in data_set:
        classification = solver.classify(entry)
        print("{}\t\t{}".format(classification, entry))
        if classification == entry.classification:
            correct_count += 1

    print('Accuracy: {}%'.format(correct_count / len(data_set) * 100))
