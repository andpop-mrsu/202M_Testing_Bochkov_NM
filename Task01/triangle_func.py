class IncorrectTriangleSides(Exception):
    pass


def get_triangle_type(a, b, c):
    """
    >>> get_triangle_type(3, 3, 3)
    'equilateral'
    >>> get_triangle_type(5, 5, 3)
    'isosceles'
    >>> get_triangle_type(4, 5, 6)
    'nonequilateral'
    >>> get_triangle_type(0, 1, 2)
    Traceback (most recent call last):
        ...
    IncorrectTriangleSides: Стороны должны быть положительными числами
    >>> get_triangle_type(1, 2, 3)
    Traceback (most recent call last):
        ...
    IncorrectTriangleSides: Треугольник с такими сторонами не существует
    >>> get_triangle_type('a', 2, 3)
    Traceback (most recent call last):
        ...
    IncorrectTriangleSides: Стороны должны быть числами
    """
    try:
        a_float = float(a)
        b_float = float(b)
        c_float = float(c)
    except (TypeError, ValueError):
        raise IncorrectTriangleSides("Стороны должны быть числами")
    
    if any(side <= 0 for side in (a_float, b_float, c_float)):
        raise IncorrectTriangleSides("Стороны должны быть положительными числами")
    
    if (a_float + b_float <= c_float) or (a_float + c_float <= b_float) or (b_float + c_float <= a_float):
        raise IncorrectTriangleSides("Треугольник с такими сторонами не существует")
    
    if a_float == b_float == c_float:
        return "equilateral"
    elif a_float == b_float or a_float == c_float or b_float == c_float:
        return "isosceles"
    else:
        return "nonequilateral"


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)