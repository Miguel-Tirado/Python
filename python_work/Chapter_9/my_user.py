from users import Admin

miguel = Admin('miguel','tirado','sacramento','engineer')
miguel.describe_user()

miguel_list = [
    'can reset password',
    'can moderate discussions',
    'can suspend accounts',
]

miguel.priviliges.privileges = miguel_list
print(f"\nThe admin {miguel.first} {miguel.last} has these privileges: " )
miguel.priviliges.show_privileges()