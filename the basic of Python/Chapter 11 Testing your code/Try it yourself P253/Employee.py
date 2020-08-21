import unittest

class Employee(self, first_name, last_name, annual_salary):
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = int(annual_salary)

    def give_raise(self, raise_amount=''):
        try:
            if raise_amount:
                self.annual_salary = self.annual_salary + int(raise_amount)
            else:
                self.annual_salary = self.annual_salary + 5000
        except ValueError:
            print("Please enter a valid number.")

class Test_Employ(unittest.TestCase):
    def setUp(self):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = int(annual_salary)

    def test_give_default_raise(self):


if __name__ == '__main__':



