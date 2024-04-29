"""
run test file
import test module
"""

from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    def test_add_numbers(self):
        response = calc.add(5,10)

        self.assertEqual(response,15)