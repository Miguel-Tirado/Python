name = 'ada lovelace'
# note the '.' after the name.title() tells python to make the title method act on the variable name
print(name.title())

# note that '' and "" are the same in python 
# f indicates a f string for format 
first_name = 'ada'
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

# here I added hello and changed the case of full name varibale to be more formal like 
print(f"Hello, {full_name.title()}!")
# here is anther way of printing the same thing
msg = f"Hello, {full_name.title()}!"
print(msg)
