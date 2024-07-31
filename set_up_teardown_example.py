import unittest

import pytest


class setup_teardown_example(unittest.TestCase):

    def setUp(self):
        print('into set up \n')
        driver = selenium_base.selenium_start('https://www.nike.com')

    def test_1(self):
        print("into test1 \n")

    def test_2(self):
        print("into test2 \n")
        assert 5 == 5

    def test_3(self):
        print("into test3 \n")
        assert 5 == 5

    def tearDown(self):
        print('into tear down')
