
import math

class Value:
    def __init__(self, data, children=(), op='', label='') -> None:
        self.data = data
        self.label = label
        self._prev = set(children)
        self._op = op

    def __repr__(self) -> str:
        return f'Value data={self.data}'

    def __add__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data + other.data, (self, other), '+')
        return out

    def __mul__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data * other.data, (self, other), '*')
        return out

    def tanh(self):
        x = self.data
        t = ((math.exp(x)**2) - 1)/((math.exp(x)**2) + 1)
        out = Value(t, (self, ), 'tanh')
        return out


# Inputs
x1 = Value(3.0, label='x1')
x2 = Value(0.0, label='x2')

# Weights
w1 = Value(-5.0, label='w1')
w2 = Value(100.0, label='w2')

# bias
b = Value(6.7, label='b')

x1w1 = x1 * w1; x1w1.label = 'x1w1'
x2w2 = x2 * w2; x2w2.label = 'x2w2'
x1w1x2w2 = x1w1 + x2w2; x1w1x2w2.label = 'x1w1 + x2w2'
n = x1w1x2w2 + b; n.label = 'n'
o = n.tanh(); o.label = 'o'
print(o)
