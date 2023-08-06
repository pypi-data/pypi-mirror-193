import unittest
from pandas import DataFrame
from random_filters.src.random_filters.random_checkbox import get_random_checkbox
from random_filters.src.random_filters.random_combobox import combobox_hierarchy


class TestGetRandomCheckbox(unittest.TestCase):
    def test_returns_string(self):
        result = get_random_checkbox()
        self.assertIsInstance(result, str)

    def test_returns_one_of_given_checkboxes(self):
        checkboxes = ['almoco', 'jantar', 'final de semana', 'dia de semana']
        result = get_random_checkbox(checkboxes, probability=1)
        self.assertIn(result, checkboxes)

    def test_returns_empty_string_when_no_checkbox_is_selected(self):
        result = get_random_checkbox(probability=0)
        self.assertEqual(result, '')


class TestComboboxHierarchy(unittest.TestCase):
    def setUp(self):
        self.data_dict = {
            "Estado": ["SP", "SP", "SP", "SC", "SC", "SC"],
            "Cidade": ["São Paulo", "Itatiba", "Campinas", "Chapecó", "Xaxim", "Xanxerê"]
        }
        self.data_df = DataFrame(self.data_dict)

    def test_returns_string(self):
        result = combobox_hierarchy(self.data_dict)
        self.assertIsInstance(result, str)

    def test_no_hierarchy(self):
        data = {"Estado": ["SP", "SC"], "Cidade": ["São Paulo", "Chapecó"]}
        with self.assertRaises(AssertionError):
            combobox_hierarchy(data)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            combobox_hierarchy(1)
