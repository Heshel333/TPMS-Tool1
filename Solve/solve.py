import numpy as np


def create_grid(q):
    base_grid = np.mgrid[0:2*np.pi:q, 0:2*np.pi:((2 * np.pi) / (q.imag - 1)) * 0.86602]

    board = np.zeros(len(base_grid[0].ravel()))
    board[1::2] = (np.pi / (q.imag - 1))

    base_grid_x = base_grid[0].ravel() + board
    base_grid_y = base_grid[1].ravel()

    grid_out = np.vstack((base_grid_x, base_grid_y)).T

    return grid_out


grid = create_grid(200j).T


def count_points_z(z, form, th1, th2):

    points = (
        tuple(grid[0][i[0]] for i in enumerate(form(grid[0], grid[1], z * 2 * np.pi)) if -th1 / 2 < i[1] < th2 / 2),
        tuple(grid[1][i[0]] for i in enumerate(form(grid[0], grid[1], z * 2 * np.pi)) if -th1 / 2 < i[1] < th2 / 2)
    )

    transparent = 1 - (len(points[0]) / len(grid[0]))

    return points, transparent


def count_transparent(form, th1, th2):
    transparent = []
    q = 200
    for z in np.linspace(0, 1, q):
        points = tuple(grid[0][i[0]] for i in enumerate(form(grid[0], grid[1], z * 2 * np.pi)) if -th1 / 2 < i[1] < th2 / 2)
        transparent.append(1 - (len(points) / len(grid[0])))

    data = np.vstack((np.array(transparent), np.linspace(0, 1, q)))

    return data


