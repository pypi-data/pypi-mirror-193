import numpy as np
import re
from variable_lib_drturtle.variables import *
from dataclasses import dataclass


U_RE = re.compile(r"^(?P<name>.+?)(?:\((?P<unit>.+)\))?$", flags=re.MULTILINE)

DIM_MAP = {"x": 0, "y": 1, "z": 2}


@dataclass
class Value1D:
    """Represents one dimension of an X value.
    Do not set these to a variable, but retrieve them from an instance.
    """

    name: str
    unit: str
    values: np.ndarray

    @property
    def with_unit(self):
        """Returns the current value of the variable, plus its unit.

        :rtype: str
        """
        return f"{self.value} {self.unit}"

    @property
    def name_val(self):
        """Returns the name, unit, and current value of the variable.

        :rtype: str
        """
        return f"{self.name}: {self.with_unit}"

    @property
    def value(self):
        """Returns the most recent value"""
        return self.values[-1]

    def __getitem__(self, key: int):
        return self.values[key]

    def __len__(self):
        return len(self.values)


class NDVariable:
    def __init__(self, initial, name: str):

        if isinstance(initial, list):
            initial = np.array(initial)

        if isinstance(initial, np.ndarray):
            self.shape = initial.shape[0]
        else:
            self.shape = 1

        if isinstance(initial, int) or isinstance(initial, float):
            initial = np.array([initial])

        match = U_RE.match(name)
        self.unit = (match.group("unit") or "").strip()
        self.var_name = match.group("name").strip()
        self.name = f'{self.var_name}{f" ({self.unit})" if self.unit else ""}'.strip()

        self.vals = np.array([initial])

    def append(self, *args):
        """Creates a 1D array and appends it to the list."""
        arr = np.array([*args])
        self.add(arr)

    def add(self, arr: np.ndarray):
        """Adds an array to the list.

        :param arr: The next value to add.
        :type arr: np.ndarray
        """
        self.vals = np.vstack((self.vals, arr))

    @property
    def value(self):
        if self.shape == 1:
            return self.vals[-1][0]
        return self.vals[-1]

    def get(self, dim: str):
        """Gets the X, Y, or Z dimension."""
        di = DIM_MAP[dim]
        if self.shape <= di:
            raise IndexError("Invalid dimension for this variable.")

        return Value1D(f"{dim.upper()} {self.name}", self.unit, self.vals.T[di])

    @property
    def x(self):
        return self.get("x")

    @property
    def y(self):
        return self.get("y")

    @property
    def z(self):
        return self.get("z")

    @property
    def with_unit(self):
        """Returns the current value of the variable, plus its unit.

        :rtype: str
        """
        return f"{self.value} {self.unit}"

    @property
    def name_val(self):
        """Returns the name, unit, and current value of the variable.

        :rtype: str
        """
        return f"{self.name}: {self.with_unit}"

    def __getitem__(self, key: int):
        return self.values[key]

    def __len__(self):
        return len(self.values)

    def __iadd__(self, other):
        """Adds other to the last value, then appends"""
        if self.shape == 1 and not isinstance(other, np.ndarray):
            other = np.array([other])
        else:
            if not isinstance(other, np.ndarray):
                raise ValueError("Other must be ndarray")
            elif other.shape != self.value.shape:
                print(other, self.value)
                raise ValueError(f"Other must have the same shape. {self.value.shape}")
        self.add(self.value + other)
        return self

    def __isub__(self, other):
        if self.shape == 1 and not isinstance(other, np.ndarray):
            other = np.array([other])
        else:
            if not isinstance(other, np.ndarray):
                raise ValueError("Other must be ndarray")
            elif other.shape != self.value.shape:
                print(other, self.value)
                raise ValueError(f"Other must have the same shape. {self.value.shape}")
        self.add(self.value - other)
        return self

    def __add__(self, other):
        return self.value + other

    def __sub__(self, other):
        return self.value - other

    def __mul__(self, other):
        return self.value * other

    def __div__(self, other):
        return self.value / other

    def __pow__(self, other):
        return self.value**other

    def __rdiv__(self, other):
        return other / self.value

    def __rmul__(self, other):
        return other * self.value

    def __radd__(self, other):
        return other + self.value

    def __rsub__(self, other):
        return other - self.value


x = NDVariable([0, 0], "Position (m)")
x += np.array([0, 0])
print(x.vals)
t = NDVariable(0, "Distance Travelled (m)")
for _ in range(100):
    t -= 10
print(t.name_val)
