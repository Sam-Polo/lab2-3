import unittest
from main import Tests, Factorial, Fibonacci, Exponent


class TestPolindromTrue(unittest.TestCase):
    def setUp(self):
        self.tests = Tests()

    def test_polindrom(self):
        self.assertTrue(self.tests.Polindrom('leps spel'))


class TestPolindromFalse(unittest.TestCase):
    def setUp(self):
        self.tests = Tests()

    def test_polindrom(self):
        self.assertFalse(self.tests.Polindrom('leps'))


class TestFactorial1(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(Factorial(5), 120)


class TestFactorial2(unittest.TestCase):
    def test_factorial(self):
        with self.assertRaises(Exception):
            Factorial(-10)


class TestFibonacci1(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(Fibonacci(7), 8)


class TestFibonacci2(unittest.TestCase):
    def test_fibonacci(self):
        with self.assertRaises(Exception):
            Fibonacci(-3)


class TestSimpleTrue(unittest.TestCase):
    def setUp(self):
        self.tests = Tests()

    def test_simple(self):
        self.assertTrue(self.tests.Simple(11))


class TestSimpleFalse(unittest.TestCase):
    def setUp(self):
        self.tests = Tests()

    def test_simple(self):
        self.assertFalse(self.tests.Simple(10))


class TestExponent1(unittest.TestCase):
    def test_Exponent(self):
        self.assertEqual(Exponent(2, 3), 8)


class TestExponent2(unittest.TestCase):
    def test_Exponent(self):
        self.assertAlmostEqual(Exponent(3.0, 2.0), 9.0)


class TestSort1(unittest.TestCase):
    def setUp(self):
        self.tests = Tests()

    def test_sort(self):
        array1 = [5, 3, 8, 1]
        self.assertEqual(self.tests.Sort(array1), [1, 3, 5, 8])


class TestSort2(unittest.TestCase):
    def setUp(self):
        self.tests = Tests()

    def test_sort(self):
        array1 = [10, -2, 0, 6]
        self.assertEqual(self.tests.Sort(array1), [-2, 0, 6, 10])


if __name__ == '__main__':
    unittest.main()
