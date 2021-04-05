from admin import Admin

user1 = Admin('Miguel','Tirado','Sacramento','engineer')
user1.describe_user()

user_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
]

user1.priviliges.privileges = user_privileges
print(f"The admin {user1.first} {user1.last} has these prviliges: ")
user1.priviliges.show_privileges()