import unittest
import yaml


from pipeline.input_pipeline import InputPipeline
from exceptions.exception import DatabaseNotFound

config = yaml.load(open('config.yml'))


class TestInputPipeline(unittest.TestCase):
    def setUp(self):

        super(TestInputPipeline, self).setUp()
        self.input_pipe = InputPipeline()



    def test_invalid_db(self):
        self.assertRaises(self.input_pipe.get_data_in_df('invaliddb'), DatabaseNotFound)


    def test(self):
        self.test_invalid_db()
        #self.test_invalid()

    def tearDown(self):
        super(TestInputPipeline, self).tearDown()
        self.reco_handler = None


if __name__ == '__main__':
    unittest.main()
