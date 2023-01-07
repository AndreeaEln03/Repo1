import unittest
from unittest import TestCase

import HtmlTestRunner

from Exercitii import Test


class CheckBoxTextTest:
    pass


class TestSuite(TestCase):
    def test_suite(self):
        tests = unittest.TestSuite()
        tests.addTest([unittest.defaultTestLoader.loadTestsFromTestCase(CheckBoxTextTest),
                       unittest.defaultTestLoader.loadTestsFromTestCase(Test)
                       ])
        runner =HtmlTestRunner.HTMLTestRunner(
        combine_reports= True,
        report_title ='First suite test',
        report_name ='Test Restult',
        )
        runner.run(tests)