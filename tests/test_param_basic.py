import pytest

# @pytest.mark.parametrize(
#     "n, expected",
#     [(1, True), (0, False), (-3, False), (pytest.param(2, False, marks=pytest.mark.xfail(reason="проверка xfail")))],
#     ids = ["pos","zero","neg","test_xfail"])
# def test_is_positive(n, expected):
#     assert (n>0) is expected


@pytest.mark.parametrize(
    "a, b, expected",
    [(2,3,5), (-1,1,0), (100,200,300), (0,0,0), (pytest.param(100, 100, 300,marks=pytest.mark.xfail(reason="Тест xfail")))],
    ids = [("2+3"), ("-1+1"), ("100+200"), ("0+0"), ("Тест xfail")])
def test_add(a, b, expected):
    assert a + b == expected