import pytest

from Project.Modules.ErrorHandler.error_handler import ErrorHandler


# Fixtures

@pytest.fixture
def errorhandler():
    return ErrorHandler()


# Helpers

def test_file_not_found(capsys, errorhandler):
    # arrange
    path = '/does_not_exist.json'
    
    # act
    with pytest.raises(SystemExit):
        errorhandler.file_not_found(path)
    out, err = capsys.readouterr()
    
    # assert
    assert out == path + "  file could not be found\n"


# def test(errorhandler):
#     assert 'true' == 'true'

