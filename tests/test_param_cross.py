import pytest

@pytest.mark.parametrize("numbers", [[1,2,3], []], ids=("list123", "empty"))
@pytest.mark.parametrize("operation", ["sum", "len"],ids=("sum", "len"))
def test_math_operation(numbers, operation):

    expected_map = {
        ("sum", (1,2,3)):6,
        ("sum", ()):0,
        ("len", (1,2,3)): 3,
        ("len", ()): 0
    }

    key = (operation, tuple(numbers))
    expected = expected_map[key]
    actual = sum(numbers) if operation == "sum" else len(numbers)

    assert actual == expected