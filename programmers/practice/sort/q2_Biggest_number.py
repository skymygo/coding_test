#1 simple test
def solution_1(numbers):
    numbers = list(map(str, numbers))
    return ''.join(sorted(numbers, reverse=True))

#2 Added Compare Function and Implemente Quick Sort
def compare_function(a, b):
    return a+b > b+a

def solution(numbers):
    numbers =list(map(str, numbers))

    pivot_stack = [[0,len(numbers)-1]]
    while len(pivot_stack) > 0: # first pivot
        left, right = pivot_stack.pop()
        pivot_value, pl, pr = numbers[left], left+1, right
        while pl<pr:
            while compare_function( pivot_value, numbers[pr]) and pl < pr: pr -= 1
            while compare_function( numbers[pl], pivot_value) and pl < pr: pl+=1
            numbers[pl], numbers[pr] = numbers[pr], numbers[pl]
            if pl != pr:
                pl +=1
                pr -=1
        if compare_function(numbers[pl], pivot_value): numbers[left], numbers[pl] = numbers[pl], numbers[left]
        if(left+1 < pl): pivot_stack.append([left, pl-1])
        if(pr < right): pivot_stack.append([pr, right])

    if numbers[0] == '0': return '0'
    return ''.join(numbers)


#Other People Solution (best in my criteria)
import functools

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer

#Reflection My Code
import functools

def compare_function(a, b):
    if a+b > b+a: return 1
    else: return -1

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(compare_function), reverse=True)
    answer = str(int(''.join(n)))
    return answer


#Other People Solution (This is very Pythonic)
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))


if __name__ == '__main__':
    input = [[6,10,2], [3,30,34,5,9]]
    output = ['6210', '9534330']

    for _input, _output in zip(input, output):
        pred = solution(_input)
        print('[{}]\tinput: {}\toutput: {}\tpred: {}'.format(pred==_output, _input, _output, pred))

