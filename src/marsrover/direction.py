class Direction:
    def __init__(self, direction):
        self._direction = direction

    def rotate_left(self):
        self._direction = self.get_left_side(self._direction)

    def rotate_right(self):
        self._direction = self.get_right_side(self._direction)

    @staticmethod
    def get_left_side(direction):
        left_side_of = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}
        return left_side_of[direction]

    @staticmethod
    def get_right_side(direction):
        right_side_of = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
        return right_side_of[direction]

    def __str__(self):
        return self._direction

    def __eq__(self, other):
        return self._direction == other
