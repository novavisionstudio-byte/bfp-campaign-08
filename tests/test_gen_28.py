from app.gen_28 import value_28


def test_value_28():
    assert value_28(2) == 2 * 4 + 1
    assert value_28(0) == 1
