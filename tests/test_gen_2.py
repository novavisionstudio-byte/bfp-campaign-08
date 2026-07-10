from app.gen_2 import value_2


def test_value_2():
    assert value_2(2) == 2 * 8 + 2
    assert value_2(0) == 2
