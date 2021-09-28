from dataclasses import dataclass


@dataclass
class Grid:
    _max_width: int
    _max_height: int

    def max_height(self) -> int:
        return self._max_height

    def max_width(self) -> int:
        return self._max_width
