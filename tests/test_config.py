import unittest

import tests.mock_files as files
import sleeper_analyzer.utils as utils
from sleeper_analyzer.config import Config


class TestConfig(unittest.TestCase):

    def setUp(self):
        utils.rm_tree(files.TEMP_FOLDER)

    def tearDown(self):
        utils.rm_tree(files.TEMP_FOLDER)

    def test_config_save(self):
        config = Config(files.TEMP_FOLDER)
        config['key'] = 'value'
        config.save()
        saved_config = utils.load_json_file(files.TEMP_FOLDER / 'config.json')
        self.assertEqual(saved_config['key'], 'value')

    def test_config_load(self):
        config = Config(files.TEST_DATA_FOLDER)
        config.load()
        self.assertEqual(config['last_update'], '2022-12-06T09:48:53.240102')
