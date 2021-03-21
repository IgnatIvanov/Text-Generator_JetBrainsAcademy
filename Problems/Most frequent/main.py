from collections import Counter

text = ("all I want is a proper cup of coffee made in a proper copper coffee pot. "
        "I may be off my dot but I want a cup of coffee from a proper coffee pot.")

for obj in Counter(text.split()).most_common(int(input())):
    print(obj[0], obj[1])
