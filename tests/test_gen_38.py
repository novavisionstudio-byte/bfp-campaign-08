from app.gen_38 import value_38


def test_value_38():
    assert value_38(2) == 2 * 6 + 8
    assert value_38(0) == 8
