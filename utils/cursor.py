class Cursor(object):
    x: int
    y: int
    max_x: int
    max_y: int

    def __init__(self, max_x: int, max_y: int) -> None:
        self.max_x = max_x
        self.max_y = max_y
        self.x = self.max_x // 2 - 15
        self.y = self.max_y // 2 - 8

    def get_x(self) -> int:
        return self.x

    def get_y(self) -> int:
        return self.y

    def set_x(self, x: int) -> None:
        self.x += x

    def set_y(self, y: int) -> None:
        self.y += y

    def reset_x(self) -> None:
        self.x = self.max_x // 2 - 15

    def reset_y(self) -> None:
        self.y = self.max_y // 2 - 8
