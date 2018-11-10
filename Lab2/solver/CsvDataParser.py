from Lab2.solver.DataEntry import DataEntry


def read_data(file_name, classification_index=-1):
    content = [line.rstrip() for line in open(file_name)]

    result = []

    for line in content:
        data = line.split(',')
        classification = data.pop(classification_index)
        result.append(DataEntry(data, classification))

    return result
