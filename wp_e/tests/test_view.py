import requests
import unittest
import json
import os
import csv


 
class TestDependencies(unittest.TestCase):

    def test_json(self):
        try:
            import json
        except ModuleNotFoundError:
            self.fail("JSON not imported")

    def test_csv(self):
        try:
            import csv
        except ModuleNotFoundError:
            self.fail("CSV not imported")
    
    def test_requests(self):
        try:
            import requests
        except ModuleNotFoundError:
            self.fail("Requests not imported")
    
    def test_sys(self):
        try:
            import sys
        except ModuleNotFoundError:
            self.fail("SYS not imported")


class TestAPIMethods(unittest.TestCase):

    def test_get_api_returns_200(self):
        response = requests.get("http://interview.wpengine.io/v1/accounts/")
        assert response.status_code == 200

    def test_get_api_instance_returns_200(self):
        response = requests.get("http://interview.wpengine.io/v1/accounts/2")
        assert response.status_code == 200




if __name__ == '__main__':
    unittest.main()