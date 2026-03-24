class Point2D:
    """Point in (x, y) coordinate space)."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_point(self):
        print(f"({self.x:.2f}, {self.y:.2f})")

    def __eq__(self, other):
        if isinstance(other, Point2D):
            return self.x == other.x and self.y == other.y
        return False

    def __str__(self):
        return f"({self.x:.2f}, {self.y:.2f})"


p1 = Point2D(1.234, 0.23456)
p2 = Point2D(-1, 3)

p1.print_point()   # (1.23, 0.23)
p2.print_point()   # (-1.00, 3.00)

p6 = Point2D(1, 2)
p7 = Point2D(1, 2)

print(p6 == p7)   # True -- == kontrollib kas nende väärtus on sama
print(p6 is p7)   # False -- is kontrollib kas on tegu sama objektiga

p8 = p6
print(p6 is p8)   # True

p1 = Point2D(1, 2)
print(p1)           # (1.00, 2.00)