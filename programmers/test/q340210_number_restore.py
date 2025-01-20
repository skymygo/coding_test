# https://school.programmers.co.kr/learn/courses/30/lessons/340210

def solution(expressions):
    answer = [_ for _ in expressions if _.endswith("X")]
    hints = [_ for _ in expressions if not (_.endswith("X"))]

    number_exp = max([int(_) for _ in " ".join(expressions) if _.isnumeric()]) + 1
    is_certi = False

    if number_exp == 9:
        is_certi = True
    else:
        for hint in hints:
            number_1, exp_symbol, number_2, _, res = hint.split(" ")
            number_1 = [int(_) for _ in number_1[::-1]]
            number_2 = [int(_) for _ in number_2[::-1]]
            res = [int(_) for _ in res[::-1]]

            if number_exp == 9:
                is_certi = True
                break

            if exp_symbol == "+":
                for n1, n2, n_r in zip(number_1, number_2, res):
                    if n1 + n2 == n_r:
                        continue
                    else:
                        number_exp = n1 + n2 - n_r
                        is_certi = True
                        break

            if exp_symbol == "-":
                for n1, n2, n_r in zip(number_1, number_2, res):
                    if n1 - n2 == n_r:
                        continue
                    else:
                        number_exp = n_r + n2 - n1
                        is_certi = True
                        break

    new_answer = []
    for i in range(len(answer)):
        number_1, exp_symbol, number_2, _, res = answer[i].split(" ")
        number_1 = [int(_) for _ in number_1[::-1]]
        number_2 = [int(_) for _ in number_2[::-1]]
        res = ""
        buf = 0
        if len(number_1) < len(number_2):
            number_1, number_2 = number_2, number_1

        if exp_symbol == "+":
            for n1, n2 in zip(number_1, number_2):
                if n1 + n2 + buf < number_exp:
                    res += str(n1 + n2 + buf)
                    buf = 0
                else:
                    if is_certi:
                        res += str(n1 + n2 + buf - number_exp)
                        buf = 1
                    else:
                        res = "?"
                        break
        if exp_symbol == "-":
            for n1, n2 in zip(number_1, number_2):
                if n1 >= (n2 + buf):
                    res += str(n1 - (n2 + buf))
                    buf = 0
                else:
                    if is_certi:
                        res += str(number_exp + n1 - (n2 + buf))
                        buf = 1
                    else:
                        res = "?"
                        break
        if res != "?":
            if len(number_1) > len(number_2):
                if exp_symbol == "+":
                    if number_1[-1] + buf < number_exp:
                        res += str(number_1[-1] + buf)
                    else:
                        res += "0"
                        res += "1"
                    buf = 0
                else:
                    res += str(number_1[-1] - buf)
                    buf = 0
            if buf == 1:
                res += str(buf)
            res = res[::-1]
            res = res.lstrip("0")
            if res == "":
                res = "0"
        answer[i] = answer[i].replace("X", res)
    return answer


# print(solution(["14 + 3 = 17", "13 - 6 = X", "51 - 5 = 44"]))
# print(solution(["1 + 1 = 2", "1 + 3 = 4", "1 + 5 = X", "1 + 2 = X"]))
# print(solution(["10 - 2 = X", "30 + 31 = 101", "3 + 3 = X", "33 + 33 = X"]))
# print(solution(["2 - 1 = 1", "2 + 2 = X", "7 + 4 = X", "5 - 5 = X"]))
# print(solution(["2 - 1 = 1", "2 + 2 = X", "7 + 4 = X", "8 + 4 = X"]))
#
# print()
print(solution(["2 - 1 = X", "3 + 3 = X"]))
print(solution(["1 - 1 = X", "1 + 1 = X"]))
print(solution(["14 + 3 = X", "7 + 7 = X"]))
print(solution(["33 - 20 = X"]))
print(solution(["46 - 33 = X"]))
print(solution(["5 + 3 = X", "8 + 8 = X"]))
print(solution(["88 + 88 = X"]))
print(solution(["88 - 11 = X"]))
print(solution(["88 - 0 = X"]))
print(solution(["8 + 81 = X", "8 + 8 = X"]))
print(solution(["41 + 4 = X", "1 + 4 = 10"]))
print(solution(["41 - 4 = X", "1 + 4 = 10"]))
print(solution(["41 - 32 = X", "1 + 4 = 10"]))
