from app.gen_9 import value_9


def test_value_9():
    assert value_9(2) == 2 * 8 + 3
    assert value_9(0) == 3
