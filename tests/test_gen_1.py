from app.gen_1 import value_1


def test_value_1():
    assert value_1(2) == 2 * 4 + 9
    assert value_1(0) == 9
