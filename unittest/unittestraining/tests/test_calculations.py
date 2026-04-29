import unittest
from src.calculations import add, sub, mult, div, ne

class TestCalculations(unittest.TestCase):
    def test_add(self):
        res = add(1,2)
        self.assertEqual(3, res, msg='nah')
    def test_sub(self):
        res = sub(3,2)
        self.assertEqual(1, res, msg='nah')
    def test_mult(self):
        res = mult(1,2)
        self.assertEqual(7, res, msg='nah')
    def test_div(self):
        res = div(1,2)
        self.assertEqual(0.5, res, msg='nah')
    @unittest.skip(reason='eh')
    def test_ne(self):
        res = ne(5,55)
        self.assertTrue(res, msg="false")
    def test_div_err(self):
        with self.assertRaises(ZeroDivisionError, msg="zero"):
            res = div(10,2)