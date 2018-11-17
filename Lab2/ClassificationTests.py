import random


# Returns a tuple of (data_left, data_poped)
def pop_random_elements(data, count):
    if len(data) < count:
        return [], data.copy()

    poped = []
    left = data.copy()
    while len(poped) < count:
        index = random.randint(0, len(left) - 1)
        poped.append(left.pop(index))

    return left, poped


def k_part_split(data, k):
    result = []
    left = data.copy()
    single_count = int(len(data) / k)
    for i in range(k):
        left, new_part = pop_random_elements(left, single_count)
        result.append(new_part)

    if len(left) > 0:
        for i in range(len(left)):
            result[i].append(left[i])

    return result


def base_test(solver, learning_data, testing_data):
    correct_count = 0
    solver.set_learning_data(learning_data)
    print('class\t\tdata')
    for entry in testing_data:
        classification = solver.classify(entry)
        print("{}\t\t{}".format(classification, entry))
        if classification == entry.classification:
            correct_count += 1

    return correct_count / len(testing_data) * 100


def train(solver, data_set):
    accuracy = base_test(solver, data_set, data_set)
    print('Accuracy: {}%'.format(accuracy))


def split(solver, data_set, percentage_split):
    count = int(len(data_set) * percentage_split)
    testing_set, learning_set = pop_random_elements(data_set, count)

    accuracy = base_test(solver, learning_set, testing_set)
    print('Accuracy: {}%'.format(accuracy))


def k_fold(solver, data_set, k):
    parts = k_part_split(data_set, k)

    accuracy_sum = 0
    for i in range(k):
        temp = parts.copy()
        testing_set = temp.pop(i)
        learning_set = []
        for x in temp:
            learning_set += x

        accuracy_sum += base_test(solver, learning_set, testing_set)

    print('Accuracy: {}%'.format(accuracy_sum / k))
