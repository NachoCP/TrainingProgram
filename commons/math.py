import numpy as np


def cosine_similarity(A, B):
    return np.dot(A, B) / (np.linalg.norm(A) * np.linalg.norm(B))


def normalize(value, min_value, max_value):
    if max_value == min_value:
        return 1.0
    return (value - min_value) / (max_value - min_value)
