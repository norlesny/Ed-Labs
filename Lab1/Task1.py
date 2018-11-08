import matplotlib.pyplot as plt
import numpy as np


def generate_data(a, b, c):
    coeffs = np.linspace(0, 1, 10)
    x = []
    y = []

    for lambda1 in coeffs:
        coeffs2 = np.linspace(0, 1 - lambda1, 10)
        for lambda2 in coeffs2:
            lambda3 = 1 - lambda1 - lambda2

            x.append(lambda1 * a[0] + lambda2 * b[0] + lambda3 * c[0])
            y.append(lambda1 * a[1] + lambda2 * b[1] + lambda3 * c[1])

    return x, y


a = [-1, 4]
b = [2, 0]
c = [0, 0]

x, y = generate_data(a, b, c)
plt.plot(x, y, 'ro')
plt.plot(x, y)
plt.margins(0.05)
plt.show()
