import pytest

list_1 = [1, 2, 3]


@pytest.fixture()
def list_():
    return list_1
