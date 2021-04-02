from itertools import combinations
from collections import Counter

def solution(orders, course):
    course_list = list()
    for order in orders:
        for c in course:
            course_list.extend(combinations(sorted(order),c))
    count = Counter(course_list)
    course_list = list()
    len_list = [0] * course[-1]
    for key,value in count.most_common():
        if value >1 and len(key) in course and len_list[len(key)-1] <= value:
            len_list[len(key)-1] = value
            course_list.append(''.join(key))
    course_list.sort()

    return course_list



if __name__ == '__main__':
    input = [[["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]], [["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]],
             [["XYZ", "XWY", "WXA"], [2,3,4]],]
    output = [["AC", "ACDE", "BCFG", "CDE"], ["ACD", "AD", "ADE", "CD", "XYZ"], ["WX", "XY"]]

    for _input, _output in zip(input, output):
        res = solution(*_input)
        print('{}, input: {}, output: {}, predict: {}'.format(res==_output, _input, _output, res))

