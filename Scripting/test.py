def spam():
	global eggs
	eggs = eggs + 1
	print(eggs)
eggs = 42 
spam()
print(eggs)