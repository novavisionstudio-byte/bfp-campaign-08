from app.gen_40 import value_40


def test_value_40():
    assert value_40(2) == 2 * 8 + 7
    assert value_40(0) == 7
