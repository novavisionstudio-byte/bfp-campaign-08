from app.gen_12 import value_12


def test_value_12():
    assert value_12(2) == 2 * 6 + 1
    assert value_12(0) == 1
