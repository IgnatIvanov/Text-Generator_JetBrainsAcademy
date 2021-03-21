from collections import Counter

in_data = input()

freq_counter = Counter(in_data.split())

print(freq_counter.most_common(1)[0][0])
