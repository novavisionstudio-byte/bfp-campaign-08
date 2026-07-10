from app.gen_30 import value_30


def test_value_30():
    assert value_30(2) == 2 * 8 + 1
    assert value_30(0) == 1
