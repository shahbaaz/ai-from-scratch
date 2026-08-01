
from vector2d import Vector2D

a = Vector2D(1, 2)
b = Vector2D(3, 5)

def test_add():
    assert a + b == Vector2D(4, 7)

def test_sub():
    assert a - b == Vector2D(-2, -3)

def test_mul():
    assert a * 5 == Vector2D(5, 10)

def test_rmul():
    assert 5 * a == Vector2D(5, 10)

def test_eq():
    assert a != b
    c = Vector2D(3, 5)
    assert b == c

def test_abs():
    d = Vector2D(3, 4)
    assert abs(d) == 5