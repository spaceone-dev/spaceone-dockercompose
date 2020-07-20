import os
import uuid
import unittest
import random

from langcodes import Language

from spaceone.core.utils import random_string
from spaceone.core.unittest.runner import RichTestRunner

from spaceone.tester import TestCase, print_json

class TestRootDomain(TestCase):


    def test_create_root_domain(self):
        ...

if __name__ == "__main__":
    unittest.main(testRunner=RichTestRunner)
