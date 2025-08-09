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