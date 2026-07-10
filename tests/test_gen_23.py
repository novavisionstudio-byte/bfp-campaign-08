from app.gen_23 import value_23


def test_value_23():
    assert value_23(2) == 2 * 2 + 5
    assert value_23(0) == 5
