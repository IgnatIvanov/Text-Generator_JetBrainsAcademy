# Write your code here
from nltk.tokenize import WhitespaceTokenizer
import nltk
nltk.download('punkt')

filename = str(input())
f = open(filename, "r", encoding="utf-8")  # Opening file with corpus

corpus = f.read()  # Reading corpus from a file

wt = WhitespaceTokenizer()
tokens = wt.tokenize(corpus)  # Tokenizing corpus
# Calculating and printing statistics
print('Corpus statistics')
print('All tokens:', len(tokens))
print('Unique tokens:', len(set(tokens)))
# print(sorted(set(tokens)))
print('')

user_input = input()
while user_input != 'exit':

    try:
        print(tokens[int(user_input)])
    except IndexError:
        print('Index Error. Please input an integer that is in the range of the corpus.')
    except TypeError:
        print('Type Error. Please input an integer.')
    except ValueError:
        print('Type Error. Please input an integer.')
    finally:
        user_input = input()
