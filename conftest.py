import pytest

@pytest.hookimpl
def pytest_addoption(parser):
    parser.addoption('--app', action='store', default="ios", help="Choose App: ios or android")


@pytest.fixture(scope="session")
def app(request):
    return request.config.getoption("--app")


# @pytest.fixture(scope='session', autouse=True)
# def session_setup_teardown():
#     yield
#     notify_slack()
