import random


def train(solver, data_set):
    correct_count = 0
    solver.set_learning_data(data_set)
    print('class\t\tdata')
    for entry in data_set:
        classification = solver.classify(entry)
        print("{}\t\t{}".format(classification, entry))
        if classification == entry.classification:
            correct_count += 1

    print('Accuracy: {}%'.format(correct_count / len(data_set) * 100))


def split(solver, data_set, percentage_split):
    testing_set = data_set.copy()
    learning_set = []
    number_of_learning_elements = int(len(data_set) * percentage_split)
    while len(learning_set) < number_of_learning_elements:
        index = random.randint(0, len(testing_set) - 1)
        learning_set.append(testing_set.pop(index))

    correct_count = 0
    solver.set_learning_data(learning_set)
    print('class\t\tdata')
    for entry in testing_set:
        classification = solver.classify(entry)
        print("{}\t\t{}".format(classification, entry))
        if classification == entry.classification:
            correct_count += 1

    print('Accuracy: {}%'.format(correct_count / len(testing_set) * 100))
