import numpy as np


def mult_scalar(x: float, y: float) -> float:
    return x * y


def mult_mat(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    return x @ y
