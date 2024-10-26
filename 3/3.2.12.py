import unittest

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        self.assertEqual(abs(42), 42, "Должно являться модулем числа")
    def test_abs2(self):
        self.assertNotEqual(abs(42), -42, "Не может являться модулем числа")
    def test_abs2(self):
        self.assertEqual(3, -42, "Всегда падает")

if __name__ == "__main__":
    unittest.main()
