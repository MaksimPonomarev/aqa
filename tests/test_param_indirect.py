import pytest

@pytest.mark.parametrize(
    "numbers, expected",
    [("small", 6), ("empty", 0), ("neg", -6)],
    indirect=["numbers"],
    ids=("small", "empty", "neg"))
def test_sum_numbers(numbers, expected):
    assert sum(numbers) == expected