import unittest
from Tests.lesson_12.homeworks import sum_numbers
from Tests.lesson_12.homeworks import part_payment
from Tests.lesson_12.homeworks import even_numbers
from Tests.lesson_12.homeworks import Square

class TestSumNumbers(unittest.TestCase):
    def test_sum_numbers_positive(self):
        result = sum_numbers("1,2,3,4")
        self.assertEqual(result, 10)

    def test_sum_numbers_char(self):
        result = sum_numbers("qwerty1,2,3")
        self.assertEqual(result, 'Не числове значення')

class TestPartPayment(unittest.TestCase):
    def test_part_payment_positive(self):
        result = part_payment(3, 1500)
        self.assertEqual(result, 4500)

    def test_part_payment_not_even(self):
        result = part_payment(3, 1500)
        self.assertNotEqual(result, 4400)

    def test_part_payment_negative(self):
        result = part_payment(-3, 1500)
        self.assertEqual(result, 'Wrong data')

    def test_part_payment_float(self):
        result = part_payment(3, 1500.65)
        self.assertEqual(result, 'Month cant be float')

class TestEvenNumbers(unittest.TestCase):
    def test_even_numbers_positive(self):
        result = even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 6, 2])
        self.assertEqual(result, 28)

    def test_even_numbers_odds(self):
        result = even_numbers([1, 7, 3, 5, 7, 9, 7])
        self.assertEqual(result, 0)

class TestSquare(unittest.TestCase):
    def test_square_per(self):
        result = Square(3)
        self.assertEqual(result.perimeter(), 12)

    def test_square_area(self):
        result = Square(3)
        self.assertEqual(result.area(), 9)

if __name__ == '__main__':
    unittest.main()