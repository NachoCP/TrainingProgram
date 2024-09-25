import numpy as np
import pytest

from commons.math import cosine_similarity, normalize


def test_cosine_similarity_identical_vectors():
    # Prueba con vectores idénticos
    A = np.array([1, 0, 0])
    B = np.array([1, 0, 0])
    result = cosine_similarity(A, B)
    assert result == np.float64(1.0)

def test_normalize_standard_case():
    # Prueba con valores normales
    value = 5
    min_value = 0
    max_value = 10
    result = normalize(value, min_value, max_value)
    assert result == pytest.approx(0.5)
