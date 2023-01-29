import unittest
from utils.dict import get_val

class TestGetVal(unittest.TestCase):
    def test_get_val(self):
        data = {"vcs": "mercurial"}
        self.assertEqual(get_val(data, "vcs"), 'mercurial')
        self.assertEqual(get_val(data, "vcs", "git"), 'mercurial')
        self.assertEqual(get_val(data, "cs", "git"), "git")
        self.assertEqual(get_val({}, "vcs", "bazaar"), "bazaar")

