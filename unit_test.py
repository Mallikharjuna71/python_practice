import unittest

def add(x, y):
    return x+y

def div(x, y):
    if x==0:
        raise ZeroDivisionError
    return x/y

class TestingPractice(unittest.TestCase):
    def setUp(self):
        self.a = 12
        self.b = 13

    def tearDown(self):
        pass

    def test_adding(self):
        self.assertEqual(add(12, 13), 25)
        self.assertRaises(ZeroDivisionError, div, 12, 0)
        self.assertIn(5, [1, 3, 5])