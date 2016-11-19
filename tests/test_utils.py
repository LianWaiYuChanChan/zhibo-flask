import unittest
from zhibo import utils


class TestUtils(unittest.TestCase):
    def test_add(self):
        self.assertEqual(3, utils.add(1, 2))
