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

    print(highest_ig)
    print(highest_ig_index)


data = CsvDataParser.read_data('test2.csv')
print(data)

highest_info_gain_index(data)

root = TreeNode('Matematyka')
node = TreeNode('Biologia')

root.add_node(3, TreeNode('NIE'))
root.add_node(4, node)
root.add_node(5, TreeNode('NIE'))

node.add_node(3, TreeNode('TAK'))
node.add_node(4, TreeNode('NIE'))
node.add_node(5, TreeNode('TAK'))

print(root)