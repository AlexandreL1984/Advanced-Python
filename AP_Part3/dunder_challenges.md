from time import now

class Class_1:
  """
  This is documentation 1.
  My class just has one attribute: bill
  """

  bill = 5


class Class_2:
  """
  This is documentation 2.
  This class has the following:
  Class Attributes: attr, name
  Class Methods: greet
  """
  name = 'rishov'
  attr = 'I am greeting'

  @classmethod
  def greet(cls):
    return cls.name + cls.attr

class Class_3:
  """
  This is documentation 3.
  This class has:
  Class Attributes: version
  Object Attributes: starting_number, nums
  Object Methods: view_num, mean
  Class Methods: view_current_time
  """
  version = 1

  def __init__(self, n):
    self.starting_number = n
    self.nums = list(range(n))

  def view_num(self):
    print(self.starting_number)
    return self.starting_number

  def mean(self):
    return sum(self.nums) / len(self.nums)

  @classmethod
  def view_current_time(cls):
    fmt_timestamp = f"Version {cls.version} accessed at {now()}"

    print(fmt_timestamp)

    return fmt_timestamp
"""
    Challenge:

    Return the documentation from each class inside a .txt file called dunder_challenge_docs.txt
"""
