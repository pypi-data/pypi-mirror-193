G = 6.674 * (10**-11)  # constant G
import numpy as np
import matplotlib.pyplot as plt


def Gravity(m1: float, m2: float, pos1: np.ndarray, pos2: np.ndarray):
    """Calculate gravitational force between two objects"""

    # setting up radius vector (sun to earth)
    r = pos2 - pos1  # creates the radius vector of sun to earth
    rmag = np.linalg.norm(r)  # normalizes the radius vecotr
    rhat = r / rmag  # unit vector for radius

    # define force object 2 exerts on object 1
    return (G * m1 * m2) / (rmag**2) * rhat


def Gfield(
    obj_m: float, obj_pos: np.ndarray, obj_radius: float, x_pos: float, y_pos: float
) -> tuple:
    """Calculate the gravitational force for two object for use in a quiver plot."""
    r = np.array([x_pos, y_pos]) - obj_pos  # radius vector
    r_mag = np.linalg.norm(r)

    # ensure 2nd object outside obj
    if r_mag <= obj_radius:
        return 0, 0

    r_hat = r / r_mag  # direction of vector
    grav = (-(G * obj_m) / (r_mag**2)) * r_hat
    return grav


def sct(x, y, x_axis, y_axis, title, **kwargs):
    plt.scatter(x, y, **kwargs)
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    plt.title(title)
    return plt


def quiver(
    x: np.ndarray,
    y: np.ndarray,
    u,
    v,
    x_axis: str = "x",
    y_axis: str = "y",
    title="x vs y",
    **kwargs
):
    plt.quiver(x, y, u, v, **kwargs)
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    plt.title(title)
    return plt
