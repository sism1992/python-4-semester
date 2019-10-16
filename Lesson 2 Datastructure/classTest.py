class Monkey:
    def __init__(self, name, age):
       self.name = name
       self.age = age

Thomas = Monkey('Thomas', 23)

Monkeys = [Thomas]

print(Monkeys[0].name)