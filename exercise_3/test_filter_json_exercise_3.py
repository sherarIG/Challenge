import unittest
from exercise_3 import filter_json
from test_consts_exercise_3 import string_json_1,\
                                   list_of_keys_1,\
                                   expected_result_1,\
                                   list_of_keys_2,\
                                   expected_result_2



class TestFilterJson(unittest.TestCase):

    def test_filter_json(self):
        result_1 = filter_json(string_json_1, list_of_keys_1)
        self.assertEqual(result_1, expected_result_1)
        result_2 = filter_json(string_json_1, list_of_keys_2)
        self.assertEqual(result_2, expected_result_2)


