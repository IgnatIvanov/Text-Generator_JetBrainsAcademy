# `random_dict` has been defined
# the input is in the variable `word`
# write the rest of the code here

random_dict.setdefault(word, 'Not in the dictionary')
print(random_dict[word])


fruit_dictionary = {}
fruit_dictionary.setdefault("apple", "green")
fruit_dictionary.setdefault("banana", "yellow")
fruit_dictionary.setdefault("orange", "orange")
print(fruit_dictionary.setdefault("apple", "red"))