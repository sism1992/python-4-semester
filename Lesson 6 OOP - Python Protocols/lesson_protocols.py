l = [1, 2, 3, 4]
l2 = [3, 5, 4]
print(l + l2)
s = 'hej'
s2 = 'Uuuuu'
print(s + s2)

class S:
    def __init__(self):
        self.name = 'Simon'
        self.sir = 'Smith'

    def __repr__(self):
        return str(self._dict_)

    def __str__(self):
        return self.name

    def __add__(self, other):
        return self.name + other.name

    def __call__(self):
        return 'blabla'

s = S()
print(repr(s))
s2 = S()
print(s + s2)