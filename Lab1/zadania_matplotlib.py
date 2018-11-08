#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D # Without this projection='3d' is not recognized
from coeffs import generate_coeffs


def draw_contour_2d(points):
    """Draws contour of the 2D figure based on the order of the points.

    :param points: list of numpy arrays describing nodes of the figure.
    """
    xs, ys = zip(points[-1], *points)
    plt.plot(xs, ys, color="blue")


def draw_contour_3d(points, sides):
    """Draws contour of the 3D figure based on the description of its sides.

    :param points: list of numpy arrays describing nodes of the figure.
    :param sides: list containing description of the figure's sides. Each side is described by a list of indexes of elements in points.
    """
    for side in sides:
        xs, ys, zs = [], [], []
        for s in side:
            xs.append(points[s][0])
            ys.append(points[s][1])
            zs.append(points[s][2])
        # Adding connection to the first node
        a = points[side[0]]
        xs.append(a[0])
        ys.append(a[1])
        zs.append(a[2])
        plt.plot(xs, ys, zs, color="blue")


def convex_comb_general(points, limit=1.0, res_arange=0.1, tabs=""):
    """Generates all linear convex combinations of points with the specified precision.

    :param points: list of numpy arrays describing nodes of the figure.
    :param limit: value to be distributed among remaining unassigned linear coefficients.
    :param res_arange: step in arange.
    :param tabs: indent for debug printing.
    :return: list of points (each represented as np.array) being a result of all linear convex combinations.
    """

    new_points = []
    coeffs = generate_coeffs(len(points), res_arange)
    # Iterating over all coefficients
    for i in range(len(coeffs)):
        current_coeffs = coeffs[i]
        new_point = []
        # Iterating over all the points dimensions
        for dimension in range(len(points[0])):
            sum = 0
            # Iterating over all the points
            for j in range(len(current_coeffs)):
                sum += points[j][dimension] * current_coeffs[j]

            new_point.append(sum)

        new_points.append(new_point)

    return new_points


def draw_figure(x, y):
    plt.plot(x, y, "ro")


def draw_convex_combination_2d(points):
    cc_points = convex_comb_general(points, res_arange=0.1)
    # TODO: Zadanie 4.2: Rysowanie wykresu dla wygenerowanej listy punktów (cc_points).
    x=[]
    y=[]
    for p in cc_points:
        x.append(p[0])
        y.append(p[1])
    draw_figure(x, y)

    # Drawing contour of the figure (with plt.plot).
    draw_contour_2d(points)


def draw_convex_combination_3d(points, sides=None, color_z=True, res_arange=0.1):
    fig = plt.figure()
    # To create a 3D plot a sublot with projection='3d' must be created.
    # For this to work required is the import of Axes3D: "from mpl_toolkits.mplot3d import Axes3D"
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    cc_points = convex_comb_general(points, res_arange=res_arange)
    # TODO: Zadanie 4.3: Zaimplementuj rysowanie wykresu 3D. Możesz dodatkowo zaimplementować kolorowanie względem wartości na osi z.
    x = []
    y = []
    z = []
    for point in cc_points:
        x.append(point[0])
        y.append(point[1])
        z.append(point[2])

    if color_z:
        colors = []
        for i in np.linspace(0, 1, len(z)):
            colors.append([1-i, i, 0])

        ax.scatter(x, y, z, c=colors)
    else:
        ax.scatter(x, y, z)

    # Drawing contour of the figure (with plt.plot).
    if sides is not None:
        draw_contour_3d(points, sides)


def draw_vector_addition(vectors, coeffs):
    start = np.array([0.0, 0.0])
    end = np.array([0.0, 0.0])
    for v, c in zip(vectors, coeffs):
        assert isinstance(v, np.ndarray)
        assert isinstance(c, float)
        # TODO: Zadanie 4.4: Wzorując się na poniższym użyciu funkcji quiver, napisz kod rysujący czarne wektory składowe.
        # TODO: Pamiętaj podczas dodawania o ich przeskalowaniu przez odpowiedni współczynnik.
        # TODO: Po każdej iteracji start powinno zawierać punkt w którym kończyło się ostatnie przesunięcie.
        end[0] = start[0] + v[0] * c
        end[1] = start[1] + v[1] * c

        print("start: "+str(start[0])+" "+str(start[1])+"; end: "+str(end[0])+" "+str(end[1]))

        plt.quiver(start[0], start[1], end[0] - start[0], end[1] - start[1], width=0.008, color="green",
                   scale_units='xy', angles='xy', scale=1, zorder=4)

        start = end.copy()

    plt.quiver(0, 0, start[0], start[1], width=0.008, color="magenta", scale_units='xy',
               angles='xy', scale=1, zorder=4)

    # Drawing the final vector being a linear combination of the given vectors.
    # The third and the fourth arguments of the quiver function indicate movement (dx, dy), not the ending point.
    # plt.quiver(0.0, 0.0, start[0], start[1], width=0.008, color="magenta", scale_units='xy', angles='xy', scale=1, zorder=4)
    plt.margins(0.05)


def draw_triangle():
    points = [np.array([-1, 4]),
              np.array([2, 0]),
              np.array([0, 0])]
    draw_convex_combination_2d(points)
    plt.show()

def draw_rectangle():
    points = [np.array([0, 0]),
              np.array([0, 1]),
              np.array([1, 1]),
              np.array([1, 0])]
    draw_convex_combination_2d(points)
    plt.show()

def draw_hexagon():
    points = [np.array([1, -2]),
              np.array([-1, -2]),
              np.array([-2, 0]),
              np.array([-1, 2]),
              np.array([1, 2]),
              np.array([2, 0])]
    draw_convex_combination_2d(points)
    plt.show()

def draw_not_convex():
    points = [np.array([0, 0]),
              np.array([0, 2]),
              np.array([1, 1]),
              np.array([2, 3]),
              np.array([2, 0])]
    draw_convex_combination_2d(points)
    plt.show()

def draw_tetrahedron():
    sides = [[0,1,2], [1,2,3], [0,2,3], [0,1,3]]
    points = [np.array([1.0, 1.0, 1.0]),
              np.array([-1.0, -1.0, 1.0]),
              np.array([-1.0, 1.0, -1.0]),
              np.array([1.0, -1.0, -1.0])]
    draw_convex_combination_3d(points, sides=sides, color_z=True)
    plt.show()

def draw_cube():
    sides = [[0,1,2,3], [4,5,6,7], [0,4,5,1], [2,6,7,3]]
    points = [np.array([0.0, 0.0, 0.0]),
              np.array([1.0, 0.0, 0.0]),
              np.array([1.0, 1.0, 0.0]),
              np.array([0.0, 1.0, 0.0]),
              np.array([0.0, 0.0, 1.0]),
              np.array([1.0, 0.0, 1.0]),
              np.array([1.0, 1.0, 1.0]),
              np.array([0.0, 1.0, 1.0])]
    draw_convex_combination_3d(points, sides=sides, color_z=True, res_arange=0.2)
    plt.show()

def draw_vector_addition_ex1():
    v = [np.array([-1, 4]),
         np.array([2, 0]),
         np.array([0, 0])]
    coeffs = [0.4, 0.3, 0.3]
    draw_convex_combination_2d(v)
    draw_vector_addition(v, coeffs)
    plt.show()

    coeffs = [0.2, 0.8, 0.0]
    draw_convex_combination_2d(v)
    draw_vector_addition(v, coeffs)
    plt.show()



if __name__ == "__main__":
    draw_triangle()
    # draw_rectangle()
    # draw_hexagon()
    # draw_not_convex()
    # draw_tetrahedron()
    # draw_cube()
    # draw_vector_addition_ex1()
