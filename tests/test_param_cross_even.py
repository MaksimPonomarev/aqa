import pytest

@pytest.mark.parametrize("list_nums", [[2,6,4], [1,2,3]], ids=["2,6,4","1,2,3"])
@pytest.mark.parametrize("test_mode", ["all_even", "any_even"], ids=("all_even", "any_even"))
def test_params(list_nums, test_mode):
    if test_mode == "all_even":
        assert all(num % 2 == 0 for num in list_nums)

    elif test_mode == "any_even":
        assert any(num % 2 == 0 for num in list_nums)


