import unittest
max_integer = __import__("6-max_integer").max_integer

class TestMaxInteger(unittest.TestCase):
    def test_positive_integers(self):
        """Test for positive integers both ordered and unordered"""
        self.assertEqual(max_integer([9, 13, 16, 21]), 21)
        self.assertEqual(max_integer([413, 267,190, 106]), 413)
        self.assertEqual(max_integer([32, 57, 93, 21]), 57)

    def test_negative_integers(self):
        """Test for negative numbers"""
        self.assertEqual(max_integer([-9, -13, -16, -21]), -9)
        self.assertEqual(max_integer([-413, -267, -190, -106]), -106)
        self.assertEqual(max_integer([-32, -57, -93, -21]), -21)

    def test_floats(self):
        """Test for floats"""
        self.assertEqual(max_integer([1.45, 5.6, 7.01,0.968]), 7.01)
    def test_one_arg(self):
        """Test for one argument"""
        self.assertEqual(max_integer([952]), 952)

    def test_no_arg(self):
        """Test for no argument"""
        self.assertIsNone(max_integer())

    def test_empty_list(self):
        """Test for an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_mixed_data_types(self):
        """Test for mixed data types"""
        some_list = [34, 68, "strin", 77]
        with self.assertRaises(TypeError):
            max_integer(some_list)

if __name__ == "__main__":
    unittest.main()
