from app.gen_36 import value_36


def test_value_36():
    assert value_36(2) == 2 * 7 + 8
    assert value_36(0) == 8
