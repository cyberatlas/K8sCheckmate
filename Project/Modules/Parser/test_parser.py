import pytest

from Project.Modules.Parser.parser import Parser


class TestParser():
    def __init__(self):
        self.__parser_test = Parser()

    def test_load_chart_file(self):
        # arrange
        file = 'Project/TestCharts/values.yaml'
        dict1 = {}

        # act
        dict_check = self.__parser_test.load_chart(file)

        # assert
        assert dict1.viewitems() < dict_check.viewitems()

    #def test_loadchart_nofile(self):

# def test_get_max_open_ports_found_returns_value():
#     # arrange
#     dictionary = { 'max_open_ports': 4 }

#     # act
#     out = _pp.get_max_open_ports(dictionary)

#     # assert
#     assert out == 4

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
