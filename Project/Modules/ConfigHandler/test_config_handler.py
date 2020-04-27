import pytest

from Project.Modules.ConfigHandler.config_handler import ConfigHandler


# Fixtures 

@pytest.fixture
def confighandler():
    return ConfigHandler()


# Helpers

def test_get_config(confighandler):
    # arrange
    
    # act
    conf = confighandler.get_config()

    # assert
    assert conf['chartPath'] == 'Project/TestCharts/Chart.yaml'
    assert conf['policyPath'] == 'Project/TestCharts/policy.yaml'
    assert conf['valuesPath'] == ["Project/TestCharts/test1.yaml", "Project/TestCharts/test2.yaml"]
    assert conf['outputPath'] == 'Project/Output'