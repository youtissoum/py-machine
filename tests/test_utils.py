from Python_Machine.Utils import get_opposite_direction, get_loc_from_direction, do_nothing
from Python_Machine.Enums import Direction

def test_get_opposite_direction():
    assert get_opposite_direction(Direction.RIGHT) == Direction.LEFT, "Getting the opposite of right did not give left"
    assert get_opposite_direction(Direction.DOWN) == Direction.UP, "Getting the opposite of down did not give up"
    assert get_opposite_direction(Direction.LEFT) == Direction.RIGHT, "Getting the opposite of left did not give right"
    assert get_opposite_direction(Direction.UP) == Direction.DOWN, "Getting the opposite of up did not give down"

def test_get_loc_from_direction():
    assert get_loc_from_direction(15, 71, Direction.UP) == (15, 72), "loc from dir test 1 fail"
    assert get_loc_from_direction(654, 424, Direction.LEFT) == (653, 424), "loc from dir test 2 fail"
    assert get_loc_from_direction(99999999999, 0, Direction.RIGHT) == (100000000000, 0), "loc from dir test 3 fail"
    assert get_loc_from_direction(0, 0, Direction.DOWN) == (0, -1), "loc from dir test 4 fail"

def test_do_nothing():
    assert do_nothing() == None, "how"