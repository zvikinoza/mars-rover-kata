from src.marsrover.rover import Rover
from src.marsrover.grid import Grid


def test_init() -> None:
    assert Rover(Grid(10, 10)).execute('') == '0:0:N'


def test_left_rotation() -> None:
    assert Rover(Grid(10, 10)).execute('L') == '0:0:W'
    assert Rover(Grid(10, 10)).execute('LL') == '0:0:S'
    assert Rover(Grid(10, 10)).execute('LLL') == '0:0:E'
    assert Rover(Grid(10, 10)).execute('LLLL') == '0:0:N'


def test_right_rotation() -> None:
    assert Rover(Grid(10, 10)).execute('R') == '0:0:E'
    assert Rover(Grid(10, 10)).execute('RR') == '0:0:S'
    assert Rover(Grid(10, 10)).execute('RRR') == '0:0:W'
    assert Rover(Grid(10, 10)).execute('RRRR') == '0:0:N'


def test_move_forward() -> None:
    assert Rover(Grid(10, 10)).execute('F') == '0:1:N'
    assert Rover(Grid(10, 10)).execute('FFFFF') == '0:5:N'


def test_rotation_and_forward_move() -> None:
    assert Rover(Grid(10, 10)).execute('RF') == '1:0:E'
    assert Rover(Grid(10, 10)).execute('RLFFF') == '0:3:N'
    assert Rover(Grid(10, 10)).execute('RLRFFLL') == '2:0:W'
    assert Rover(Grid(10, 10)).execute('RRRRFFF') == '0:3:N'


def test_rotation_and_backward_move() -> None:
    assert Rover(Grid(10, 10)).execute('RRRB') == '1:0:W'
    assert Rover(Grid(10, 10)).execute('RRBBBR') == '0:3:W'
    assert Rover(Grid(10, 10)).execute('RRRBB') == '2:0:W'
    assert Rover(Grid(10, 10)).execute('RRLRRBBB') == '3:0:W'


def test_top_wraparound() -> None:
    assert Rover(Grid(10, 10)).execute('F' * 10) == '0:0:N'
    assert Rover(Grid(10, 10)).execute('F' * 15) == '0:5:N'


def test_bottom_wraparound() -> None:
    assert Rover(Grid(10, 10)).execute('B' * 2) == '0:8:N'
    assert Rover(Grid(10, 10)).execute('B' * 15) == '0:5:N'


def test_left_wraparound() -> None:
    assert Rover(Grid(10, 10)).execute('B' * 3) == '0:7:N'
    assert Rover(Grid(10, 10)).execute('L' + ('F' * 3)) == '7:0:W'


def test_right_wraparound() -> None:
    assert Rover(Grid(10, 10)).execute('R' + ('F' * 11)) == '1:0:E'
    assert Rover(Grid(10, 10)).execute('R' + ('F' * 9) + 'LLB') == '0:0:W'


#
# @given(multiplier=integers(min_value=0, max_value=20))
# def test_random(multiplier: int):
#     assert Rover(Grid(10, 10)).execute("LR" * multiplier) == "0:0:N"
