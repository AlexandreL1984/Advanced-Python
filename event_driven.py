# Numbers 1 through 100

map(lambda x: x**2, range(1,101))

list(map(lambda x: x**2, range(1,101)))

#Another way of doing this with comprehension
list(filter(lambda x: x % 2 == 0, map(lambda x: x**2, range(1,101))))

j = lambda x: True if x % 2 == 0 else False

j(1)

list(filter(lambda x: x%2 == 0, [1**2 for i in range(1,101)]))

from functools import reduce

reduce(lambda a,b: a+b, filter(lambda x: x%2 == 0, [i**2 for i in range(1,101)]))
