import pytest

from parser import Parser

 

# Fixtures

@pytest.fixture
def parser():
    return Parser()

# Helpers

def test_get_chart_dict(parser):
    # arrange 
    dictionary = {
	    "chartPath": "Project/TestCharts/Chart.yaml",
    }

    #act 
    chart = parser.get_chart_dict(dictionary)
    
    # assert
    assert chart != None
    assert chart['apiVersion'] == 'v1'


# def test_get_policy_dict_not_found_returns_error():
#     # arrange
#     filepath = ''

#     # act
#     # assert
#     with pytest.raises(FileNotFoundError):
#         assert (_pp.get_policies_dict(filepath))

# def test_get_policy_dict_found_returns_dict():
#     # arrange
#     filepath = 'Project/TestCharts/hello-world/Chart.yaml'

#     # act
#     out = _pp.get_policies_dict(filepath)

#     # assert
#     assert type(out) is dict
#     assert out.get('name') == 'hello-world'
#     assert out.get('version') == '0.1.0'
