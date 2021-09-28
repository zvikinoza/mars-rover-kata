from src.marsrover.direction import Direction
from src.marsrover.grid import Grid


class Coordinate:
    def __init__(self, x: int, y: int, grid: Grid) -> None:
        self._x = x
        self._y = y
        self._grid = grid

    def move_forward(self, direction: Direction) -> None:
        if direction == 'N':
            self._y += 1
        elif direction == 'W':
            self._x -= 1
        elif direction == 'S':
            self._y -= 1
        else:
            self._x += 1

        self.__handle_wraparound()

    def move_backward(self, direction: Direction) -> None:
        if direction == 'N':
            self._y -= 1
        elif direction == 'W':
            self._x += 1
        elif direction == 'S':
            self._y += 1
        else:
            self._x -= 1

        self.__handle_wraparound()

    def __handle_wraparound(self) -> None:
        if self._x < 0:  # wrap left border of grid
            self._x = self._grid.max_width() - 1
        elif self._x >= self._grid.max_width():  # wrap right border of grid
            self._x = 0

        if self._y < 0:  # wrap lower border of grid
            self._y = self._grid.max_height() - 1

        elif self._y >= self._grid.max_height():  # wrap top border of grid
            self._y = 0

    def __str__(self) -> str:
        return f'{self._x}:{self._y}'
