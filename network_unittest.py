import unittest
import json
from fetchFromAPIurl import *

class TestStringMethods(unittest.TestCase):

    def test_1(self):
        all_response = get_result("geoloc", ["193/23"], None, "json")
        for response in all_response:
            resp_dict = json.loads(response)
            self.assertEqual(resp_dict["status_code"], 200)

    def test_2(self):
        all_response = get_result("network-info", ["140.78.90.50"], None, "json")
        for response in all_response:
            resp_dict = json.loads(response)
            self.assertEqual(resp_dict["status_code"], 200)


    def test_3(self):
        all_response = get_result("as-overview", None, ["3333"], "json")
        for response in all_response:
            resp_dict = json.loads(response)
            self.assertEqual(resp_dict["status_code"], 200)


    def test_4(self):
        all_response = get_result("geoloc", ["292.0.0.1"], None, "json")
        for response in all_response:
            resp_dict = json.loads(response)
            self.assertEqual(resp_dict["status_code"], 400)


    def test_5(self):
        all_response = get_result("geoloc", ["192.0.0.1"], None, "xml")
        for response in all_response:
            resp_dict = json.loads(response)
            self.assertEqual(resp_dict["status_code"], 501)


if __name__ == '__main__':
    unittest.main()

