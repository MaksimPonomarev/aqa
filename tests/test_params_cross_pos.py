import pytest

@pytest.mark.parametrize("list_nums", [[1,2,3], [0,0,0], [-1,-2,-3], [1,-2,0,999],[]], ids=("1,2,3", "0,0,0", "-1,-2,-3", "1,-2,0,999", "[]"))
@pytest.mark.parametrize("test_mode", ["all_positive","any_positive"], ids=("all_positive", "any_positive") )
def test_pos(list_nums, test_mode):
    if test_mode == "all_positive":
        assert all(num > 0 for num in list_nums)
    elif test_mode == "any_positive":
        assert any(num > 0 for num in list_nums)