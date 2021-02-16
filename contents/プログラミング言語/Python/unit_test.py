import unittest


def pow(x: float) -> float:
    return x*x


class Vector2:
    """Hello, func

    Lorem ipsum dolor sit amet, 

    Args:
        arg1 (str): First argument
        arg2 (list[int]): Second argument
        arg3 (dict[str, int]): Third argument

    Returns:
        str or None: Return value

    Raises:
        ValueError: if arg1 is empty string.
    """

    def __init__(self, x: float, y: float):
        self.x = _x
        self.y = _y


class UnitTest(unittest.TestCase):

    def test_pow(self):
        value = 3
        expected = 9
        actual = pow(value)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    # unittest.main()
    print(pow(6))
    a = Vector(1, 6)
