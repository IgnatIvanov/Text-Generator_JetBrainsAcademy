import re


sentence = 'Do I like cats? Yes!!'
template = re.escape('Do I like cats? Yes!!')
tem = re.match(template, sentence)
