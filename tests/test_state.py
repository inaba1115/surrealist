import unittest

from surrealist.state import State


class TestState(unittest.TestCase):
    def test_timestamp(self):
        s = State().timestamp("+0.5")
        self.assertEqual(s.timestamp("+1.0")._timestamp, 1.5)
        self.assertEqual(s.timestamp("-1.0")._timestamp, -0.5)
        self.assertEqual(s.timestamp("*3.0")._timestamp, 1.5)
        self.assertEqual(s.timestamp("/5.0")._timestamp, 0.1)
        self.assertEqual(s.timestamp("1.0")._timestamp, 1.0)
