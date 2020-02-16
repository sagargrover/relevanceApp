import unittest
import pandas as pd
import yaml
import joblib
import requests
import numpy as np
from unittest.mock import Mock


from service.handler.reco_handler import RecoHandler


class TestAPI(unittest.TestCase):
    def setUp(self):
        super(TestAPI, self).setUp()
        self.reco_handler = RecoHandler()
        self.request = Mock()


    def test_invalid(self):
        self.request.data.return_value = {
            "text"
        }
        self.assertRaises(KeyError)



    def test_with_valid(self):
        self.request.data.return_value = {
            "text": "gnition knock (detonation) sensor senso fits 01 06 bmw 325ci 2 5l l6"
        }
        self.assertEquals(self.reco_handler(self.request), (1, 200))
        self.request.data.return_value = {
            "text": "sagar"
        }
        self.assertEquals(self.reco_handler(self.request), (0, 200))


    def test(self):
        self.test_with_valid()
        self.test_invalid()

    def tearDown(self):
        super(TestAPI, self).tearDown()
        self.reco_handler = None


if __name__ == '__main__':
    unittest.main()
