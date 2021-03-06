def greet(name):
    return f"Hi, {name}"


class Greet:
    # Creating the initial dunder method
    def __init__(self, name):
        self.name = name

        #Creating our own method
    def greet(self):
        return f"Hi, {self.name}"

my_greet = Greet('Alex')

type(my_greet)

my_greet.name

my_greet.greet()

# The Number Generator Class
class NumGen:
    # Creating the init dunder
    def __init__(self, n):
        self.nums = list(range(n))

    def even(self):
        for i in self.nums:
            if i % 2 == 0:
                yield i

    def odd(self):
        for i in self.nums:
            if i % 2 != 0:
                yield i

    def power(self, p):
        for i in self.nums:
            yield i**2


nums = NumGen(100)

type(nums)

nums.nums

list(nums.even())

list(nums.odd())


list(nums.power(2))

class Private:
    def __init__(self):
        self.__name = 'Alex'

    @property
    def name(self):
        return self.__name

my_private = Private()

my_private.name
