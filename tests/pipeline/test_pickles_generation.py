import unittest
import yaml
from os import path, remove
from unittest.mock import Mock
import joblib


from pipeline.generate_pickles import generate_pickles


config = yaml.load(open('config.yml'))


class TestPipeline(unittest.TestCase):
    def setUp(self):
        super(TestPipeline, self).setUp()
        self.test_path = config["resource_dir"] + "test/"
        self.input_pipe = Mock()
        self.input_pipe.get_data_in_df.return_value = joblib.load(self.test_path + 'input_df.pkl')
        self.classifier_file_path = self.test_path + config["pickle"]["classifier_model_file"]
        self.processor_file_path = self.test_path + config["pickle"]["preprocess_model_file"]
        remove(self.classifier_file_path)
        remove(self.processor_file_path)
        generate_pickles(self.input_pipe, self.test_path)

    def test_pickles_exist(self):
        self.assertEquals(path.exists(self.classifier_file_path), True)
        self.assertEquals(path.exists(self.processor_file_path), True)

    def check_if_output_generated(self):

        pass

    def test(self):
        self.test_pickles_exist()
        #self.test_invalid()

    def tearDown(self):
        super(TestPipeline, self).tearDown()
        self.reco_handler = None


if __name__ == '__main__':
    unittest.main()
