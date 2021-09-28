"""
Kata Description:

You are given the initial starting point (x,y) of a rover and the direction (N,S,E,W) it is facing.

The rover receives a character array of commands.

Implement commands that move the rover forward/backward (f,b).

Implement commands that turn the rover left/right (l,r).

Implement wrapping at edges. But be careful, planets are spheres.
Connect the x edge to the other x edge, so (1,1) for x-1 to (5,1),
but connect vertical edges towards themselves in inverted coordinates,
so (1,1) for y-1 connects to (5,1).

Implement obstacle detection before each move to a new square.
If a given sequence of commands encounters an obstacle,
the rover moves up to the last possible point,
aborts the sequence and reports the obstacle.
"""


from src.marsrover.coordinate import Coordinate
from src.marsrover.direction import Direction
from src.marsrover.grid import Grid


class Rover:
    def __init__(self, grid: Grid) -> None:
        self._direction = Direction('N')
        self._coordinate = Coordinate(0, 0, grid)

    def execute(self, commands: str) -> str:
        for cmd in commands:
            if cmd == 'L':
                self._direction.rotate_left()
            elif cmd == 'R':
                self._direction.rotate_right()
            elif cmd == 'F':
                self._coordinate.move_forward(self._direction)
            elif cmd == 'B':
                self._coordinate.move_backward(self._direction)
            else:
                raise Exception('Undefined Command')

        return f'{self._coordinate}:{self._direction}'
