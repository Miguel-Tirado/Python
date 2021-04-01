def greet_user(names):
    """print a simple greeting to each user in the list"""
    for name in names:
        msg = f"Hello {name.title()}"
        print(msg)

usernames = ['miggy','hannah','richard','felix']
greet_user(usernames)