from app.gen_20 import value_20


def test_value_20():
    assert value_20(2) == 2 * 2 + 7
    assert value_20(0) == 7
