def no_square(x: float, y: int) -> float:
    if x == 0:
        return 0
    print("x**x")
    _additional: int = y**y
    res: float = x**x
    return res


def string_concat(first: str, second: str) -> str:
    return f"{first} {second}" + " " + "end"
