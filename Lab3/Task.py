import math

from Lab3 import CsvDataParser
from Lab3.TreeNode import TreeNode


def entropy(data):
    values = {}
    for entry in data:
        value = str(entry)
        if value in values:
            values[value] += 1
        else:
            values[value] = 1

    count = len(data)
    sum = 0
    for x in values:
        p = values[x] / count
        sum += p * math.log(p, 2)

    return -sum


def attribute_entropy(data):
    count = len(data)
    sum = 0

    distinct_values = list(set([d[0] for d in data]))

    for v in distinct_values:
        test = [d[1] for d in data if d[0] == v]
        sum += len(test) / count * entropy(test)

    return sum


def info_gain(whole_entropy, data):
    return whole_entropy - attribute_entropy(data)


def highest_info_gain_index(data):
    whole_entropy = entropy([d.classification for d in data])
    print(whole_entropy)

    highest_ig = -1
    highest_ig_index = -1
    for a in range(len(data[0].attributes)):
        ig = info_gain(whole_entropy, [(d.attributes[a], d.classification) for d in data])
        if ig > highest_ig:
            highest_ig = ig
            highest_ig_index = a

    return highest_ig_index


def filter_data(data, index):
    filtered_data = data.copy()
    for d in filtered_data:
        del d.attributes[index]

    return filtered_data


def highest_gain_node(data):
    root_index = highest_info_gain_index(data)
    root = TreeNode(str(root_index))

    root_data = [(d.attributes[root_index], d.classification) for d in data]
    filtered_data = filter_data(data, root_index)

    distinct_values = list(set([d[0] for d in root_data]))
    for v in distinct_values:
        test = [d[1] for d in root_data if d[0] == v]
        if entropy(test) == 0:
            root.add_node(v, TreeNode(test[0]))
        else:
            pass

    return root

data = CsvDataParser.read_data('test2.csv')
print(data)

root = highest_gain_node(data)
print(root)
