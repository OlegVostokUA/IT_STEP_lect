# import unittest
from lect_18 import Calculator


# class TestCalculator(unittest.TestCase):
#
#     def setUp(self):
#         self.calc = Calculator()
#
#     def test_add(self):
#         self.assertEqual(self.calc.add(5, 5), 10)
#
#     def test_divide(self):
#         self.assertEqual(self.calc.divide(5, 0), 'Zero !!!')

# import sys
#
# class TestString(unittest.TestCase):
#     def test_upper(self):
#         self.assertEqual('foo'.upper(), 'FOO')
#
#     def test_isupper(self):
#         self.assertTrue('FOO'.isupper())
#         self.assertFalse('FOo'.isupper())
#
#     @unittest.skipUnless(sys.platform.startswith('win'), 'requires Windows')
#     def test_form(self):
#         self.fail('message')
import pytest

calc = Calculator()

def test_calculator():
    assert calc.add(5, 5) == 10

def test_calculator2():
    assert calc.divide(5, 5) == 1

def test_calculator3():
    assert calc.divide(5, 0) == 'Zero !!!'



