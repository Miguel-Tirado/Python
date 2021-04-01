def isPanlidrome(word):
    word_reverse = word[::-1]
    return word == word_reverse


print(isPanlidrome('tacocat'))