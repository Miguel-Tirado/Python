def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile1 = build_profile('albert','einstein',location='princeton',field='physics')
user_profile2 = build_profile('miguel','tirado',lcoation='CSUS',field='Computer Engineering',occupation='job seeker')
print(user_profile1)
print(user_profile2)
