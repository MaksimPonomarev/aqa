import pytest

@pytest.mark.parametrize(
    "user, expected_age",
    [({"name":"Maksim","age":20}, 20),
     ({"name":"Anna","age":30}, 30),
     ({"name":"Ivan","age":40}, 40)],
    ids=("Maksim_age", "Anna_age", "Ivan_age"))
def test_user_data(user, expected_age):
    assert user["age"] == expected_age