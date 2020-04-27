import pytest

from Project.Modules.Parser.parser import Parser

 
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
    assert type(chart['name']) == str


def test_get_policy_dict(parser):
    # arrange
    dictionary = {
        "policyPath": "Project/TestCharts/policy.yaml",
    }
    # act
    chart = parser.get_policy_dict(dictionary)
    # lst = chart['BANNED_USERS']
    # assert
    assert chart != None
    assert len(chart['BANNED_USERS']) == 3

def test_get_values_dict(parser):
    # arrange
    dictionary = {
        "valuesPath": ["Project/TestCharts/test1.yaml", "Project/TestCharts/test2.yaml"],
    }
    # act
    chart = parser.get_values_dict(dictionary)
    # assert
    assert len(chart) == 2