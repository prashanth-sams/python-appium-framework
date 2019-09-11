import pytest

@pytest.hookimpl
def pytest_addoption(parser):
    parser.addoption('--app', action='store', default="ios", help="Choose App: ios or android")

@pytest.fixture(scope="session")
def app(request):
    return request.config.getoption("--app")