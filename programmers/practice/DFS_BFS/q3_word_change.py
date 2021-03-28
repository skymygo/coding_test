def solution(begin, target, words):
    word = [_ for _ in zip(begin,target)]
    bfs_queue = [ [begin, words]]
    answer = 0
    while len(bfs_queue) > 0:
        _word, _words = bfs_queue[0].copy()
        del bfs_queue[0]
        for pos in range(len(_words)):
            if len([0 for a, b in zip(_word, _words[pos]) if a != b]) == 1:
                if _words[pos] == target: return len(words) - len(_words) +1
                _tmp_words = _words.copy()
                del _tmp_words[pos]
                bfs_queue.append([_words[pos], _tmp_words])

    return answer


if __name__ == '__main__':
    input = [["hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]], ["hit", "cog", ["hot", "dot", "dog", "lot", "log"]]]
    output = [4,0]

    for _input, _output in zip(input, output):
        pred = solution(*_input)
        print('[{}]\tinput: {}\toutput: {}\tpred: {}'.format(pred == _output, _input, _output, pred))