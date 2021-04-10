import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        """Create a instance of an employee"""
        self.my_employee = Employee('miguel','tirado',60_000)

    def test_give_default_raise(self):
        """test default give rasie method"""
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.salary,65_000)

    def test_give_custom_raise(self):
        self.my_employee.give_raise(10_000)
        self.assertEqual(self.my_employee.salary,70_000)

if __name__ == '__main__':
    unittest.main()
