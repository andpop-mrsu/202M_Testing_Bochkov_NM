import unittest
from triangle_func import get_triangle_type, IncorrectTriangleSides


class TestTriangleFunc(unittest.TestCase):
    
    def test_equilateral(self):
        self.assertEqual(get_triangle_type(3, 3, 3), "equilateral")
        self.assertEqual(get_triangle_type(5.5, 5.5, 5.5), "equilateral")
    
    def test_isosceles(self):
        self.assertEqual(get_triangle_type(5, 5, 3), "isosceles")
        self.assertEqual(get_triangle_type(4.2, 4.2, 6.1), "isosceles")
        self.assertEqual(get_triangle_type(5, 7, 7), "isosceles")
        self.assertEqual(get_triangle_type(6, 5, 6), "isosceles")
    
    def test_nonequilateral(self):
        self.assertEqual(get_triangle_type(4, 5, 6), "nonequilateral")
        self.assertEqual(get_triangle_type(3.2, 4.1, 5.7), "nonequilateral")
    
    def test_zero_side(self):
        with self.assertRaises(IncorrectTriangleSides) as context:
            get_triangle_type(0, 1, 2)
        self.assertEqual(str(context.exception), "Стороны должны быть положительными числами")
    
    def test_negative_side(self):
        with self.assertRaises(IncorrectTriangleSides) as context:
            get_triangle_type(-1, 2, 3)
        self.assertEqual(str(context.exception), "Стороны должны быть положительными числами")
    
    def test_triangle_inequality_equal(self):
        with self.assertRaises(IncorrectTriangleSides) as context:
            get_triangle_type(1, 2, 3)
        self.assertEqual(str(context.exception), "Треугольник с такими сторонами не существует")
    
    def test_triangle_inequality_less(self):
        with self.assertRaises(IncorrectTriangleSides) as context:
            get_triangle_type(1, 2, 4)
        self.assertEqual(str(context.exception), "Треугольник с такими сторонами не существует")
    
    def test_non_numeric_input(self):
        with self.assertRaises(IncorrectTriangleSides) as context:
            get_triangle_type('a', 2, 3)
        self.assertEqual(str(context.exception), "Стороны должны быть числами")
    
    def test_none_input(self):
        with self.assertRaises(IncorrectTriangleSides) as context:
            get_triangle_type(None, 2, 3)
        self.assertEqual(str(context.exception), "Стороны должны быть числами")
    
    def test_string_input(self):
        with self.assertRaises(IncorrectTriangleSides) as context:
            get_triangle_type("abc", 2, 3)
        self.assertEqual(str(context.exception), "Стороны должны быть числами")
    
    def test_boolean_input(self):
        with self.assertRaises(IncorrectTriangleSides) as context:
            get_triangle_type(True, 2, 3)
        pass


if __name__ == '__main__':
    unittest.main()