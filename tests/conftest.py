import pytest

@pytest.fixture
def yield_func():
    print("Подготовка к тесту запущена")
    users = {"age": 20, "name": "Maksim"}
    yield users
    print("Чистим данные")
    users.clear()

@pytest.fixture
def global_data():
    return "данные для всех тестов"

@pytest.fixture
def numbers(request):
    param = request.param
    if param == "small":
        return [1,2,3]
    elif param == "empty":
        return []
    elif param == "neg":
        return [-1,-2,-3]
    else:
        raise ValueError(f"Unknown param for 'numbers': {param}")

