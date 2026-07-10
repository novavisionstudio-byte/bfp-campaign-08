from app.gen_26 import value_26


def test_value_26():
    assert value_26(2) == 2 * 9 + 4
    assert value_26(0) == 4
