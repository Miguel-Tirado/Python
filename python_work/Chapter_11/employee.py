class Employee:
    """simple model of an employee"""
    def __init__(self,first,last,salary):
        """store first last name and salary of employee"""
        self.first = first
        self.last = last
        self.salary = salary
    
    def give_raise(self,money=5000):
        self.salary += money

        
        