import unittest
import tests.mock_files as files

import sleeper_analyzer.utils as utils


class TestUtils(unittest.TestCase):

    def test_load_json_file(self):
        expected = {
            "__meta__": {"version": "0.1.0"},
            "default_options": [],
            "last_update": "2022-12-06T09:48:53.240102"
        }
        config = utils.load_json_file(files.CONFIG_FILE)
        self.assertEqual(config, expected)

    def test_rm_tree(self):
        root = files.TEMP_FOLDER
        sub_folder = root / 'sub_folder'
        sub_folder.mkdir(parents=True, exist_ok=True)
        file = sub_folder / 'test.txt'
        with file.open("w") as fp:
            print('Test', file=fp)
        self.assertTrue(root.exists())
        utils.rm_tree(root)
        self.assertFalse(root.exists())
