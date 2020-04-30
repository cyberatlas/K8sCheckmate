import pytest

from Project.Modules.OutputHandler.output_handler import OutputHandler


# Fixtures

@pytest.fixture
def outputhandler():
    return OutputHandler()


# Helpers



# def test(outputhandler):
#     assert 'true' == 'true'
