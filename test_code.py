import unittest
import maths


class ClassDeTest(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(maths.addition(100, -100), 0)


if __name__ == '__main__':
    unittest.main()
