import pytest
from Project.PolicyParse import policyparse as _pp
import os

def test_get_max_open_ports_not_found_prints_error():
    # arrange
    dictionary = {}

    # act
    out = _pp.get_max_open_ports(dictionary)

    # assert
    assert out == -1

def test_get_max_open_ports_found_returns_value():
    # arrange
    dictionary = { 'max_open_ports': 4 }

    # act
    out = _pp.get_max_open_ports(dictionary)

    # assert
    assert out == 4

def test_get_policy_dict_not_found_returns_error():
    # arrange
    filepath = ''

    # act
    # assert
    with pytest.raises(FileNotFoundError): 
        assert (_pp.get_policies_dict(filepath))

def test_get_policy_dict_found_returns_dict():
    # arrange
    filepath = 'Project/TestCharts/Chart.yaml'

    # act
    out = _pp.get_policies_dict(filepath)

    # assert
    assert type(out) is dict
    assert out.get('name') == 'hello-world'
    assert out.get('version') == '0.1.0'

