from src.marsrover.direction import Direction
from src.marsrover.grid import Grid


class Coordinate:
    def __init__(self, x: int, y: int, grid: Grid):
        self._x = x
        self._y = y
        self._grid = grid

    def move_forward(self, direction: Direction):
        if direction == 'N':
            self._y += 1
        elif direction == 'W':
            self._x -= 1
        elif direction == 'S':
            self._y -= 1
        else:
            self._x += 1

        self.__handle_wraparound()

    def move_backward(self, direction: Direction):
        if direction == 'N':
            self._y -= 1
        elif direction == 'W':
            self._x += 1
        elif direction == 'S':
            self._y += 1
        else:
            self._x -= 1

        self.__handle_wraparound()

    def __handle_wraparound(self):
        if self._x < 0:
            self._x = self._grid.max_width() - 1
        if self._x >= self._grid.max_width():
            self._x = 0
        if self._y < 0:
            self._y = self._grid.max_height() - 1
        elif self._y >= self._grid.max_height():
            self._y = 0

    def __str__(self):
        return f'{self._x}:{self._y}'
