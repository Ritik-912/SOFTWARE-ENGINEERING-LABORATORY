# calculator.py

def add(a, b):
    """
    Adds two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The sum of the two numbers.

    Example:
        >>> add(2, 3)
        5
    """
    return a + b


def subtract(a, b):
    """
    Subtracts the second number from the first number.

    Args:
        a (float): The number from which b is subtracted.
        b (float): The number to subtract from a.

    Returns:
        float: The result of the subtraction.

    Example:
        >>> subtract(5, 3)
        2
    """
    return a - b


def multiply(a, b):
    """
    Multiplies two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The product of the two numbers.

    Example:
        >>> multiply(2, 3)
        6
    """
    return a * b


def divide(a, b):
    """
    Divides the first number by the second number.

    Args:
        a (float): The numerator.
        b (float): The denominator.

    Returns:
        float: The result of the division.

    Raises:
        ValueError: If b is zero.

    Example:
        >>> divide(6, 3)
        2.0
    """
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b
