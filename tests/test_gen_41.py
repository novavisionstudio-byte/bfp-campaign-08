from app.gen_41 import value_41


def test_value_41():
    assert value_41(2) == 2 * 4 + 1
    assert value_41(0) == 1
