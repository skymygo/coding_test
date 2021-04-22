from itertools import groupby
def solution(words, queries):
    words.sort(key=lambda x : len(x))
    words = {k:list(g) for k,g in groupby(words, len)}
    answer = list()

    for query in queries:
        equal_len_words = words.get(len(query), list())
        key_words = query.split("?")

        if query == "?"*len(query):
            answer.append(len(equal_len_words))
        elif query[0] == "?":
            keyword = key_words[-1]
            match_words = [word for word in equal_len_words if word.endswith(keyword)]
        else:
            keyword = key_words[0]
            match_words = [word for word in equal_len_words if word.startswith(keyword)]

        answer.append(len(match_words))

    return answer

if __name__ == "__main__":
    in_out = [
        [["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"], [3, 2, 4, 1, 0]]
    ]

    for _var in in_out:
        _input, _output = _var[:-1], _var[-1]
        pred = solution(*_input)
        print("[{}] input: {}\toutput: {}\tpred: {}".format(pred==_output, _input, _output, pred))