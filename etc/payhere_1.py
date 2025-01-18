import re

with open("../example.txt") as f:
    example_text = f.read()

def count_word(text, word):
    return len(re.findall(f'\\b{word}\\b', text.lower()))

print(count_word(example_text, "rebecca"))

from collections import Counter
import re
import time

time_1 = time.time()
def top_N_frequent_words(text, number):
    words = re.findall(r'\b\w{4,}\b', text.lower())
    word_counts = Counter(words)
    return word_counts.most_common(number)

print(top_N_frequent_words(example_text, 5))
time_2 = time.time()
print(time_2-time_1)