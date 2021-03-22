from nltk.tokenize import WhitespaceTokenizer
from nltk.util import ngrams
import nltk
import random
import re

nltk.download('punkt')

filename = str(input())  # Reading filename
f = open(filename, "r", encoding="utf-8")  # Opening file with corpus

corpus = f.read()  # Reading corpus from a file

wt = WhitespaceTokenizer()  # Creating tokenizer object
tokens = wt.tokenize(corpus)  # Tokenizing corpus


# ____________________________TRIGRAMS CREATION AND USING____________________________

trigrams = ngrams(tokens, 3)  # Creating trigrams collection

# Creating Marcov chain model for trigrams
markov_dict = {}  # Dictionary for frequency counting
bigrams_collection = []  # List of bigrams made of (trigrams[0] + trigrams[1], trigrams[2])
for trigram in trigrams:  # For every trigram
    t_head = trigram[0] + ' ' + trigram[1]  # Creating head as a set of 2 first tokens
    t_tail = trigram[2]  # And a tail as a third token
    bigrams_collection.append((t_head, t_tail))  # Storing a set in the list

# Calculating appearance frequency for every third word (or second object of set)
for bigram in bigrams_collection:  # For every bigram
    markov_dict.setdefault(bigram[0], {})  # Setting empty dictionary as default
    freq_dict = markov_dict[bigram[0]]  # Reading previous frequency data for current bigram
    tail = bigram[1]  # Reading current tail
    freq_dict.setdefault(tail, 0)  # Setting empty dictionary as default
    freq_dict[tail] += 1  # Calculating appearance frequency for current tail
    markov_dict[bigram[0]] = freq_dict  # Storing calculated frequency date


# _________________________GENERATING RANDOM TEXT_________________________

start_list = []  # List for first token to start a sentence
for i in range(10):  # Repeating sentence generation 10 times
    for bigram in bigrams_collection:  # For every bigram
        # If string of 2 word start with capital letter and don`t have sentence ending punctuation
        if re.match(r'[A-Z][a-z ]+\Z', bigram[0]) is not None:
            start_list.append(bigram[0])  # Append current string of 2 words to sentence start tokens

    first_word = random.choice(start_list)  # Choosing start for sentence randomly
    head = first_word  # Creating head as a last two words of sentence
    sentence = []  # List for current sentence storing
    sentence += [first_word]  # Append first two words to sentence
    for x in range(2):  # Repeating 2 times for creating minimal sentence length of 5 words
        keys = list(dict(markov_dict[head]).keys())
        values = list(dict(markov_dict[head]).values())
        sentence += random.choices(keys, values)  # Choosing next word of sentence randomly
        # Creating head as a last two words of sentence
        head = str('{} {}'.format(str(sentence[len(sentence) - 2]).split(' ')[-1], sentence[len(sentence) - 1]))

    exit_flag = False
    while exit_flag is not True:  # While token with sentence ending punctuation didn`t chose randomly
        # Repeat next word choosing procedure
        sentence += random.choices(list(dict(markov_dict[head]).keys()), list(dict(markov_dict[head]).values()))
        head = str('{} {}'.format(str(sentence[len(sentence) - 2]).split(' ')[-1], sentence[len(sentence) - 1]))
        # Checking for sentence ending punctuation
        if str(head).endswith('.'):
            exit_flag = True
        elif str(head).endswith('!'):
            exit_flag = True
        elif str(head).endswith('?'):
            exit_flag = True
    print(*sentence)  # Printing new sentence
