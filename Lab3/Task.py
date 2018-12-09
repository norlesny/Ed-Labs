import math

from Lab3 import CsvDataParser


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

    print(sum)


data = CsvDataParser.read_data('test2.csv')
print(data)

print(entropy([d.classification for d in data]))

attribute_entropy([(d.attributes[0], d.classification) for d in data])
