import pytest

# add an argument to set the testing environment
def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="local")