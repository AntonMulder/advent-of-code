def read_example() -> str:
    return read("example")


def read_input() -> str:
    return read("input")


def read_example_lines() -> list[str]:
    return read_lines("example")


def read_input_lines() -> list[str]:
    return read_lines("input")


def read(filename: str) -> str:
    return open(filename).read()


def read_lines(filename: str) -> list[str]:
    return read(filename).splitlines()
