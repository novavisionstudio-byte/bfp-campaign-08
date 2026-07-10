from app.gen_5 import value_5


def test_value_5():
    assert value_5(2) == 2 * 7 + 8
    assert value_5(0) == 8
