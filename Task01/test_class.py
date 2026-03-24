import pytest
from triangle_class import Triangle, IncorrectTriangleSides


class TestTriangle:

    def test_create_equilateral(self):
        t = Triangle(3, 3, 3)
        assert t.a == 3
        assert t.b == 3
        assert t.c == 3
    
    def test_create_isosceles(self):
        t = Triangle(5, 5, 3)
        assert t.a == 5
        assert t.b == 5
        assert t.c == 3
    
    def test_create_nonequilateral(self):
        t = Triangle(4, 5, 6)
        assert t.a == 4
        assert t.b == 5
        assert t.c == 6
    
    def test_create_float_sides(self):
        t = Triangle(3.5, 4.2, 5.8)
        assert t.a == 3.5
        assert t.b == 4.2
        assert t.c == 5.8
    
    def test_create_zero_side(self):
        with pytest.raises(IncorrectTriangleSides):
            Triangle(0, 1, 2)
    
    def test_create_negative_side(self):
        with pytest.raises(IncorrectTriangleSides):
            Triangle(-1, 2, 3)
    
    def test_create_triangle_inequality(self):
        with pytest.raises(IncorrectTriangleSides):
            Triangle(1, 2, 4)
    
    def test_create_non_numeric(self):
        with pytest.raises(IncorrectTriangleSides):
            Triangle("a", 2, 3)
    
    def test_create_none_value(self):
        with pytest.raises(IncorrectTriangleSides):
            Triangle(None, 2, 3)
    
    def test_type_equilateral(self):
        t = Triangle(3, 3, 3)
        assert t.triangle_type() == "equilateral"
    
    def test_type_isosceles(self):
        t1 = Triangle(5, 5, 3)
        t2 = Triangle(5, 3, 5)
        t3 = Triangle(3, 5, 5)
        assert t1.triangle_type() == "isosceles"
        assert t2.triangle_type() == "isosceles"
        assert t3.triangle_type() == "isosceles"
    
    def test_type_nonequilateral(self):
        t = Triangle(4, 5, 6)
        assert t.triangle_type() == "nonequilateral"
    
    def test_perimeter_equilateral(self):
        t = Triangle(3, 3, 3)
        assert t.perimeter() == 9
    
    def test_perimeter_isosceles(self):
        t = Triangle(5, 5, 3)
        assert t.perimeter() == 13
    
    def test_perimeter_nonequilateral(self):
        t = Triangle(4, 5, 6)
        assert t.perimeter() == 15
    
    def test_perimeter_float(self):
        t = Triangle(3.5, 4.2, 5.8)
        assert t.perimeter() == pytest.approx(13.5)
    
    @pytest.mark.parametrize("a, b, c, expected_type, expected_perimeter", [
        (3, 3, 3, "equilateral", 9),
        (5, 5, 3, "isosceles", 13),
        (4, 5, 6, "nonequilateral", 15),
        (3.5, 4.2, 5.8, "nonequilateral", 13.5),
    ])
    def test_triangle_properties(self, a, b, c, expected_type, expected_perimeter):
        t = Triangle(a, b, c)
        assert t.triangle_type() == expected_type
        assert t.perimeter() == pytest.approx(expected_perimeter)
    
    @pytest.mark.parametrize("a, b, c", [
        (0, 1, 2),
        (-1, 2, 3),
        (1, 2, 4),
        ("a", 2, 3),
        (None, 2, 3),
    ])
    def test_invalid_triangles(self, a, b, c):
        with pytest.raises(IncorrectTriangleSides):
            Triangle(a, b, c)