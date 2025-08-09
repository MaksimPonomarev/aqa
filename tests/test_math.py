import pytest

# @pytest.fixture
# def sample_num():
#     return [1,2,3]
#
# def test_sum_list(sample_num):
#     assert sum(sample_num) == 6
#
# def test_sum_list(sample_num):
#     assert sample_num[0] == 1



def test_age_dict(yield_func):
    assert yield_func["age"] == 20

def test_name_dict(yield_func):
    assert yield_func["name"] == ("Maksim")

def test_return_global_data(global_data):
    assert "данные для всех тестов" in global_data