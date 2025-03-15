import unittest
from tdd.math_operations import addition_operation, subtraction_operation


class TestMathOperations(unittest.TestCase):
    def test_additional_operation(self):
        math_additional_result = addition_operation(num_1=5, num_2=10)
        self.assertEqual(math_additional_result, 15)

    def test_subtraction_operation(self):
        math_subtraction_result = subtraction_operation(num_1=10, num_2=10)
        self.assertEqual(math_subtraction_result, 1)


if __name__ == '__main__':
    unittest.main()
