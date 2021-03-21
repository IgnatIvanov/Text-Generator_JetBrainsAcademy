from nltk.tokenize import regexp_tokenize

text = input()
num = int(input())

print(regexp_tokenize(text, '[A-Za-z]+')[num])
