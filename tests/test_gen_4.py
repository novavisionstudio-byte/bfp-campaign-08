from app.gen_4 import value_4


def test_value_4():
    assert value_4(2) == 2 * 7 + 3
    assert value_4(0) == 3
