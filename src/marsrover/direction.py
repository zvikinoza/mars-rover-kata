class Direction:
    def __init__(self, direction: str) -> None:
        self._direction = direction

    def rotate_left(self):
        self._direction = self.get_left_side(self._direction)

    def rotate_right(self):
        self._direction = self.get_right_side(self._direction)

    @staticmethod
    def get_left_side(direction: str) -> str:
        left_side_of = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}
        return left_side_of[direction]

    @staticmethod
    def get_right_side(direction: str) -> str:
        right_side_of = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
        return right_side_of[direction]

    def __str__(self) -> str:
        return self._direction

    def __eq__(self, other: str) -> bool:
        return self._direction == other
