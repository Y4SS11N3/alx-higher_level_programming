#!/usr/bin/python3
"""Matrix multiplication function."""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices.

    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.

    Raises:
        TypeError: For invalid input types.
        ValueError: If matrices can't be multiplied.

    Returns:
        list: The result of the multiplication.
    """
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all(isinstance(ele, (int, float)) for ele in
               [num for row in m_a for num in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(ele, (int, float)) for ele in
               [num for row in m_b for num in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must should be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Matrix multiplication logic
    inverted_b = [[m_b[c][r] for c in range(len(m_b))]
                  for r in range(len(m_b[0]))]
    new_matrix = [[sum(row[i] * col[i] for i in range(len(inverted_b[0])))
                   for col in inverted_b] for row in m_a]

    return new_matrix
