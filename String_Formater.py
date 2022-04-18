"""Demo module."""


def calc(x: int, y: int, z: float) -> float:
    """Calc something."""
    try:
        result = x * y * z
    except Exception as e:
        print(f"calc::{e}")
    return result


print(f"Result: {calc(5, 10, 20.0)}")
