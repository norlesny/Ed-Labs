import numpy as np


def add_coeffs(coeffs, step=0.1):
    base_coeffs = np.arange(0, 1.001, step)
    new_coeffs = []

    if len(coeffs) == 0:
        for x in base_coeffs:
            new_coeffs.append([x])
    else:
        for i in range(len(coeffs)):
            for x in base_coeffs:
                new_coeffs.append(coeffs[i] + [x])

    return new_coeffs


def remove_invalid(coeffs):
    valid_coeffs = []
    for coeff in coeffs:
        if sum(coeff) == 1:
            valid_coeffs.append(coeff)

    return valid_coeffs


def generate_coeffs(dimension, step=0.1):
    coeffs = []
    if dimension < 1:
        return coeffs

    for i in range(dimension):
        coeffs = add_coeffs(coeffs, step)

    coeffs = remove_invalid(coeffs)

    return coeffs

