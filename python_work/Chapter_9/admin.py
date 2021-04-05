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

class Privileges:
    """Simple attempt to model user privileges"""
    def __init__(self,privileges=[]):
        self.privileges = privileges
    
    def show_privileges(self):
        print(f"Privleges for user: ")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("- This user has no privileges")

class Admin(User):
    """Simple attempt to model a admin"""
    def __init__(self, first, last, location, occupation):
        super().__init__(first, last, location, occupation)
        #self.privileges = []
        self.priviliges = Privileges()
    

admin1 = Admin('miguel','tirado','sacramento','engineer')
admin1.describe_user()
admin1.priviliges.privileges = ['can add post', 'can delete post']
admin1.priviliges.show_privileges()