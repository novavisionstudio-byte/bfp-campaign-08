from app.gen_17 import value_17


def test_value_17():
    assert value_17(2) == 2 * 7 + 9
    assert value_17(0) == 9
