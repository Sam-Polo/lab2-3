import unittest


class TestCos(unittest.TestCase):
    def test_cos1(self):
        from polo_lab2 import cos
        self.assertEqual(cos(0.5), 0.8775825621589781)


class TestCos2(unittest.TestCase):
    def test_cos2(self):
        from polo_lab2 import cos
        self.assertEqual(round(cos(3.14 / 2)), 0)


class TestSin(unittest.TestCase):
    def test_sin(self):
        from polo_lab2 import sin
        self.assertEqual(sin(0.5), 0.4794255386164159)


class TestSin2(unittest.TestCase):
    def test_sun(self):
        from polo_lab2 import sin
        self.assertEqual(round(sin(3.14 / 2)), 1)


class TestLn(unittest.TestCase):
    def test_ln(self):
        from polo_lab2 import ln
        self.assertEqual(ln(0.5), -0.6931471795482411)


class TestLn2(unittest.TestCase):
    def test_ln(self):
        from polo_lab2 import ln
        with self.assertRaises(Exception) as ERROR:
            self.assertEqual((ln(-0.5)), 0)


class Test1(unittest.TestCase):
    def test_func(self):
        from polo_lab2 import sin
        from polo_lab2 import cos
        self.assertEqual(sin(0.5) + cos(0.5), 1.357008100775394)


class Test2(unittest.TestCase):
    def test_func(self):
        from polo_lab2 import sin
        from polo_lab2 import cos
        self.assertEqual(sin(0.5) - cos(0.5), -0.3981570235425622)


class Testfunc(unittest.TestCase):
    def test_func(self):
        from polo_lab2 import func
        self.assertEqual(func(-0.5), -1.9577488602923039)


class Testfunc2(unittest.TestCase):
    def test_func(self):
        from polo_lab2 import func
        self.assertEqual(func(0), "INFINITY")


class Testfunc3(unittest.TestCase):
    def test_func(self):
        from polo_lab2 import func
        self.assertEqual(func(0.5), -0.6082938777812147)
