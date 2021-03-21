# Write your code here
from nltk.tokenize import WhitespaceTokenizer
from nltk.util import bigrams
import nltk
import random
from collections import Counter

nltk.download('punkt')

filename = str(input())
f = open(filename, "r", encoding="utf-8")  # Opening file with corpus

corpus = f.read()  # Reading corpus from a file

wt = WhitespaceTokenizer()
tokens = wt.tokenize(corpus)  # Tokenizing corpus


# _________________________SINGLE TOKEN STATISTICS OUTPUT_________________________

# # Calculating and printing statistics
# print('Corpus statistics')
# print('All tokens:', len(tokens))
# print('Unique tokens:', len(set(tokens)))
# # print(sorted(set(tokens)))
# print('')
#
# user_input = input()
# while user_input != 'exit':
#
#     try:
#         print(tokens[int(user_input)])
#     except IndexError:
#         print('Index Error. Please input an integer that is in the range of the corpus.')
#     except TypeError:
#         print('Type Error. Please input an integer.')
#     except ValueError:
#         print('Type Error. Please input an integer.')
#     finally:
#         user_input = input()


# _________________________CREATING BIGRAMS_________________________

bigrams_generator = bigrams(tokens)
bigrams_collection = list(bigrams_generator)


# _________________________BIGRAMS STATISTICS AND INFO OUTPUT_________________________

# print('Number of bigrams:', len(bigrams_collection))
# print('')
# user_input = input()
# while user_input != 'exit':
#     try:
#         print('Head:', list(bigrams_collection)[int(user_input)][0], 'Tail:', list(bigrams_collection)[int(user_input)][1])
#     except IndexError:
#         print('Index Error. Please input a value that is not greater than the number of all bigrams.')
#     except TypeError:
#         print('Typ Error. Please input an integer.')
#     except ValueError:
#         print('Typ Error. Please input an integer.')
#     finally:
#         user_input = input()


# _________________________CREATING MARKOV CHAIN MODEL_________________________

markov_dict = {}

for bigram in bigrams_collection:
    markov_dict.setdefault(bigram[0], {})
    freq_dict = markov_dict[bigram[0]]
    tail = bigram[1]
    freq_dict.setdefault(tail, 0)
    freq_dict[tail] += 1
    markov_dict[bigram[0]] = freq_dict

# user_input = input()
# while user_input != 'exit':
#     print('Head:', user_input)
#     try:
#         freq_dict = dict(markov_dict[user_input])
#     except KeyError:
#         print('Key Error. The requested word is not in the model. Please input another word.')
#     else:
#         freq_dict = dict(sorted(freq_dict.items(), key=lambda item: item[1], reverse=True))
#         for obj in dict(freq_dict).items():
#             print('Tail:', obj[0], 'Count:', obj[1])
#     finally:
#         print('')
#         user_input = input()


# _________________________GENERATING RANDOM TEXT_________________________

for i in range(10):
    first_word = random.choice(tokens)
    head = first_word
    sentence = []
    sentence += [first_word]
    for x in range(9):
        sentence += random.choices(list(dict(markov_dict[head]).keys()), list(dict(markov_dict[head]).values()))
        head = sentence[len(sentence) - 1]
    print(*sentence)
    # print('')
