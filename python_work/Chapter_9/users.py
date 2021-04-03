class User:
    def __init__(self, first, last, location, occupation):
        self.first = first
        self.last = last
        self.location = location
        self.occupation = occupation
        self.login_attempts = 0
    
    def describe_user(self):
        print(f"\tuser: {self.first} {self.last}.")
        print(f"\tlives in: {self.location}.")
        print(f"\tWorks as: {self.occupation}.\n")
    
    def greet_user(self):
        print(f"Hello {self.first} {self.last}, thank you for stopping by.")

    def increment_login_attempts(self):
        """Increment the amount of login_attempts by 1"""
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """Resets the amount of login attempts to 0"""
        self.login_attempts = 0


user1 = User('miguel','tirado','sacramento','Engineer')
user2 = User('Sherry','leng','San fransico','Nurse')
user3 = User('richard','tirado','sacramento','historain')

user1.greet_user()
user1.describe_user()

user2.greet_user()
user2.describe_user()

for i in range(10):
    user3.increment_login_attempts()

print(f"The amount of login attempts by user3: {user3.login_attempts}")
user3.reset_login_attempts()
print(f"User 3 has been reset, the new amount is: {user3.login_attempts}")