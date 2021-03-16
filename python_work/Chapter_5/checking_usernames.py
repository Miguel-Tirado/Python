current_users = ['Jesus','Miggy','richard','Emily','angely']
low_user = [lower_user.lower() for lower_user in current_users]
new_users = ['santi','miggy','alex','emily','ana']

for new_user in new_users:
    if new_user in low_user:
        print("Username taken, Plz choose another username")
    else:
        print("The username is avialable, congrats.")


