from app.gen_11 import value_11


def test_value_11():
    assert value_11(2) == 2 * 6 + 1
    assert value_11(0) == 1
