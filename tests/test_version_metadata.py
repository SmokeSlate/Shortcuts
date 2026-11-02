"""Validate every updater response without calling external services."""
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class VersionMetadataTest(unittest.TestCase):
    def test_all_version_responses_are_json_objects(self):
        paths = sorted((ROOT / 'scVersions').glob('*.txt'))
        self.assertTrue(paths)
        for path in paths:
            with self.subTest(path=path.name):
                value = json.loads(path.read_text())
                self.assertIsInstance(value, dict)
                self.assertEqual(value['result'], 'success')
                self.assertIn('id', value)

    def test_beta_identifier_is_preserved(self):
        value = json.loads((ROOT / 'scVersions/updbBeta.txt').read_text())
        self.assertEqual(value['id'], 'udbBeta')

if __name__ == '__main__':
    unittest.main()
