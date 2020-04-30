import pytest

# from Project.Models.error_type import ErrorType
from Project.Modules.ValueVerifier.value_verifier import ValueVerifier

# Fixtures

@pytest.fixture
def valueverifier():
    return ValueVerifier()


"""
This testing is based off of the values that the user has setup 
and may not work once a user has added or removed thier own checks.
Also this will not test any new checks a user sets up. 
(but for code coverage we will be adding this just for completeness of testing)
"""
# Helpers

def test_port_search(valueverifier):
    # arrange 
    values_dict = {
        "port": "80",
        "image": {"repository":"nginx","tag": "stable"}
    }
    # act
    ports = valueverifier.port_search(values_dict)
    # assert
    assert ports == ['80']


def test_port_search_no_ports(valueverifier):
    # arrange 
    values_dict = {
        "port": "",
        "image": {"repository":"nginx","tag": "stable"}
    }
    # act
    ports = valueverifier.port_search(values_dict)
    # assert
    assert ports == ['']


def test_image_search(valueverifier):
    # arrange 
    values_dict = {
        "port": "80",
        "image": {"repository":"nginx","tag": "stable"}
    }
    # act
    images = valueverifier.image_search(values_dict)
    # assert
    assert images == ['nginx']


def test_port_search_no_images(valueverifier):
    # arrange 
    values_dict = {
        "port": "",
        "image": ""
    }
    # act
    images = valueverifier.port_search(values_dict)
    # assert
    assert images == ['']


def test_image_search_incorrect_layout(valueverifier):
    # arrange 
    values_dict = {
        "port": "80",
        "image": "repository"
    }
    # act
    with pytest.raises(TypeError) as err:
       # obs =  TypeError('AssertionError')
        valueverifier.image_search(values_dict)
    exception_raised = err.value
    expected = 'string indices must be integers'
    # assert
    assert str(exception_raised) == expected

# def test_check(valueverifier):
#     # arrange 
    
#     # act

#     # assert
#     assert 'true' == 'true'
