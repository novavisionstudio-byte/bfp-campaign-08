from app.gen_8 import value_8


def test_value_8():
    assert value_8(2) == 2 * 4 + 5
    assert value_8(0) == 5
