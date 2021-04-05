from user import User

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
    