import unittest, json
import pandas as pd
import yaml
import joblib
import requests
import numpy as np
from unittest.mock import Mock


from service.handler.reco_handler import RecoHandler





class TestRecoHandler(unittest.TestCase):
    def setUp(self):
        super(TestRecoHandler, self).setUp()
        config = yaml.load(open('config.yml'))
        test_dir = config["resource_dir"] + "test/"
        self.reco_handler = RecoHandler(test_dir)
        self.request = Mock()


    def test_invalid(self):
        self.request.data = json.dumps({
            "rand": "1"
        })
        self.assertRaises(KeyError)



    def test_with_valid(self):
        self.request.data = json.dumps({
            "text": "gnition knock (detonation) sensor senso fits 01 06 bmw 325ci 2 5l l6"
        })
        self.assertEquals(self.reco_handler.get_relevance(self.request), (1, 200))
        self.request.data = json.dumps({
            "text": "sagar"
        })
        self.assertEquals(self.reco_handler.get_relevance(self.request), (0, 200))


    def test(self):
        self.test_with_valid()
        #self.test_invalid()

    def tearDown(self):
        super(TestRecoHandler, self).tearDown()
        self.reco_handler = None


if __name__ == '__main__':
    unittest.main()
