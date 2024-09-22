import numpy as np


def cosine_similarity(A, B):
    return np.dot(A, B) / (np.linalg.norm(A) * np.linalg.norm(B))

def normalize(value, min_value, max_value):
    """Normaliza un valor dentro de un rango entre 0 y 1."""
    if max_value == min_value:
        return 1.0  # Evitar división por cero en caso de que todos los valores sean iguales
    return (value - min_value) / (max_value - min_value)