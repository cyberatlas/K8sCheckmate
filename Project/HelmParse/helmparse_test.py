import pytest
from Project.HelmParse import helmparse as _hp 

def test_get_yaml_file_not_found_raises_error():
    # arrange
    filepath = ''

    # act
    # assert
    with pytest.raises(FileNotFoundError): 
        assert (_hp.get_yaml(filepath))

def test_get_yaml_file_found_returns_yaml():
    # arrange
    filepath = 'Project/TestCharts/hello-world/Chart.yaml'

    # act
    out = _hp.get_yaml(filepath)

    # assert
    assert type(out) is dict
    assert out.get('apiVersion') == 'v1'
    assert out.get('appVersion') == '1.0'


