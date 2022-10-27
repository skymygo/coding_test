from itertools import groupby
from collections import Counter

def solution(words, queries):
    words.sort(key=lambda x: len(x))
    words = {k: list(g) for k, g in groupby(words, len)}
    answer = list()

    for query in queries:
        equal_len_words = words.get(len(query), list())
        key_words = query.split("?")

        if query == "?" * len(query):
            answer.append(len(equal_len_words))
            continue
        elif query[0] == "?":
            keyword = key_words[-1]
            equal_len_words = [word[-len(keyword):] for word in equal_len_words]
        else:
            keyword = key_words[0]
            equal_len_words = [word[:len(keyword)] for word in equal_len_words]

        count = Counter(equal_len_words)
        answer.append(count.get(keyword, 0))

    return answer

if __name__ == "__main__":
    in_out = [
        [["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"], [3, 2, 4, 1, 0]]
    ]

    for _var in in_out:
        _input, _output = _var[:-1], _var[-1]
        pred = solution(*_input)
        print("[{}] input: {}\toutput: {}\tpred: {}".format(pred==_output, _input, _output, pred))