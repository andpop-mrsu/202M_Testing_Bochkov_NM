class IncorrectTriangleSides(Exception):
    pass


class Triangle:
    
    def __init__(self, a, b, c):
        try:
            self.a = float(a)
            self.b = float(b)
            self.c = float(c)
        except (ValueError, TypeError):
            raise IncorrectTriangleSides("Стороны должны быть числами")
        
        if any(side <= 0 for side in (self.a, self.b, self.c)):
            raise IncorrectTriangleSides("Стороны должны быть положительными числами")
        
        if (self.a + self.b <= self.c) or (self.a + self.c <= self.b) or (self.b + self.c <= self.a):
            raise IncorrectTriangleSides("Треугольник с такими сторонами не существует")
    
    def triangle_type(self):
        """
        >>> t = Triangle(3, 3, 3)
        >>> t.triangle_type()
        'equilateral'
        >>> t = Triangle(5, 5, 3)
        >>> t.triangle_type()
        'isosceles'
        >>> t = Triangle(4, 5, 6)
        >>> t.triangle_type()
        'nonequilateral'
        """
        if self.a == self.b == self.c:
            return "equilateral"
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return "isosceles"
        else:
            return "nonequilateral"
    
    def perimeter(self):
        """
        >>> t = Triangle(3, 3, 3)
        >>> t.perimeter()
        9.0
        >>> t = Triangle(5, 5, 3)
        >>> t.perimeter()
        13.0
        >>> t = Triangle(4.5, 5.5, 6.5)
        >>> t.perimeter()
        16.5
        """
        return self.a + self.b + self.c


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)