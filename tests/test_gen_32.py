from app.gen_32 import value_32


def test_value_32():
    assert value_32(2) == 2 * 6 + 6
    assert value_32(0) == 6
