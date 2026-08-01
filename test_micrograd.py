from micrograd import Value

a = Value(2.0)
b = Value(-3.0)

def test_add():
    c = a + b
    assert c.data == -1.0

def test_multiply():
    c = a * b
    assert c.data == -6.0

def test_tanh():
    t = a.tanh()
    assert t.data == 0.9640275800758169