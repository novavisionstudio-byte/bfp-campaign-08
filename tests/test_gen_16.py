from app.gen_16 import value_16


def test_value_16():
    assert value_16(2) == 2 * 3 + 1
    assert value_16(0) == 1
