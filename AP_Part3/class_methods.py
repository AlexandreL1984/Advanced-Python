class Greet:

    attr = 'Hi'
    name = 'Alexandre'

    def __init__(self, name, second_attr):
        self.name = name
        self.attr = second_attr
        self.random_value = 2

    @classmethod
    def greet(cls):
        return cls.attr + cls.name

    @classmethod
    def getobject(cls):
        return cls(cls.attr, cls.name)

h = Greet('Sam', 'Nice')

h.attr

h.name

h.greet()

g = Greet

g.attr

g.greet()

j = g.getobject()

j.name
j.attr

j.greet()
