import pytest

@pytest.fixture(scope='fuction', autouse=True)
def setup.teardown():
    print('Fixture')
    yield
    print('ending....')