class Cursor(object):
    x: int
    y: int

    def __init__(self, x: int, y: int) -> None:
        self.x = x // 2 - 15
        self.y = y // 2 - 8

    def get_x(self) -> int:
        return self.x

    def get_y(self) -> int:
        return self.y

    def set_x(self, x: int) -> None:
        self.x += x

    def set_y(self, y: int) -> None:
        self.y += y

    def reset_x(self, x: int) -> None:
        self.x = x // 2 - 15

    def reset_y(self, y: int) -> None:
        self.y = y // 2 - 8
