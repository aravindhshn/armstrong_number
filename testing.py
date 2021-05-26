import unittest
import armstrong


class TestNumber(unittest.TestCase):
    def test_correct_number(self):
        result = armstrong.armstrong_check(153)
        self.assertTrue(result)

    def test_wrong_number(self):
        result = armstrong.armstrong_check(121)
        self.assertFalse(result)

    # def test_add(self):
    #     result = armstrong.add(5, 6)
    #     self.assertEqual(result, 11)


if __name__ == "main":
    unittest.main()
