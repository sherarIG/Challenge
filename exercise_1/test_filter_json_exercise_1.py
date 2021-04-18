import unittest
from exercise_1 import filter_json
from test_consts_exercise_1 import string_json_1,\
                                   list_of_keys_1,\
                                   expected_result_1,\
                                   string_json_2,\
                                   list_of_keys_2,\
                                   expected_result_2,\
                                   string_json_3,\
                                   list_of_keys_3,\
                                   expected_result_3


class TestFilterJson(unittest.TestCase):

    def test_filter_json(self):
        result_1 = filter_json(string_json_1, list_of_keys_1)
        self.assertEqual(result_1, expected_result_1)
        result_2 = filter_json(string_json_2, list_of_keys_2)
        self.assertEqual(result_2, expected_result_2)
        result_3 = filter_json(string_json_3, list_of_keys_3)
        self.assertEqual(result_3, expected_result_3)
