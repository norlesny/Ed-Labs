def add_coeffs(coeff, step=0.1):
    new_coeffs = []

    new_coeff = 0
    while coeff[-1] >= 0:
        new_coeffs.append(coeff+[new_coeff])

        coeff[-1] -= step
        new_coeff += step

    return new_coeffs


def generate_coeffs(dimension, step=0.1):
    if dimension <= 0:
        return []

    if dimension == 1:
        return [1]

    coeffs = [[1]]
    for i in range(dimension-1):
        new_coeffs = []
        for c in coeffs:
            new_coeffs.extend(add_coeffs(c, step))

        coeffs = new_coeffs

    return coeffs
