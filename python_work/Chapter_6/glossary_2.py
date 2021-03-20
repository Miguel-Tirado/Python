# this is a dictionary of python terms 
progamming_terms = {
    'list' : 'a collection of items in a particular order',
    'tuple' : 'is a imuttable list, which means that we cant change the items inside the list',
    'dictionary' : 'a collection of key value pairs',
    'slice' : 'is a specific group of items in a list ',
    'conditional_test' : 'an expresion that can be evaluated as true or false',
    'set' : 'a collection in which each item must be unique',
    'get()' : 'method used to set a default value that will be returned of the requested key does not exist',
    'items()' : 'method that returns a list of key value pairs',
    'keys()' : 'method that returns a list of keys, Note this is default when using for loops',
    'values()' : 'method that returns a list of values'
}

for term, meaning in progamming_terms.items():
    print(f"{term}: {meaning}.\n")