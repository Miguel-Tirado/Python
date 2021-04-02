class User:
    def __init__(self, first, last, location, occupation):
        self.first = first
        self.last = last
        self.location = location
        self.occupation = occupation
    
    def describe_user(self):
        print(f"\tuser: {self.first} {self.last}.")
        print(f"\tlives in: {self.location}.")
        print(f"\tWorks as: {self.occupation}.\n")
    
    def greet_user(self):
        print(f"Hello {self.first} {self.last}, thank you for stopping by.")


user1 = User('miguel','tirado','sacramento','Engineer')
user2 = User('Sherry','leng','San fransico','Nurse')

user1.greet_user()
user1.describe_user()

user2.greet_user()
user2.describe_user()