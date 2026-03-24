import math

def solve_quadratic(a, b, c):

    if a == 0 and b == 0 and c == 0:
        return "infinity"
    
    if a == 0 and b == 0 and c != 0:
        return None
    
    if a == 0:
        x = -c / b
        return (x,)
    
    discriminant = b**2 - 4*a*c
    
    if discriminant < 0:
        return None
    elif discriminant == 0:
        x = -b / (2*a)
        return (x, x)
    else:
        x1 = (-b - math.sqrt(discriminant)) / (2*a)
        x2 = (-b + math.sqrt(discriminant)) / (2*a)
        return (min(x1, x2), max(x1, x2))