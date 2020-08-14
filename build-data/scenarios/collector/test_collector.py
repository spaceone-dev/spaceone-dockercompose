import unittest
import uuid

from spaceone.core.unittest.runner import RichTestRunner

from spaceone.tester.unittest import TestCase, print_json


NUM_OF_COLLECTOR=1
NUM_OF_SERVERS=0   # larger than this

class TestCollector(TestCase):

    def test_all(self):
        ...

if __name__ == "__main__":
    unittest.main(testRunner=RichTestRunner)

