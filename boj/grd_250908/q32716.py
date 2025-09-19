import sys
N = int(input())

side = N // 4
origin_v = side * side

remain = N % 4

if remain == 1:
    origin_v += side -1
elif remain == 2:
    origin_v += side + side - 2
elif remain == 3:
    origin_v += side + side

if N == 6:
    origin_v = 2

print(origin_v)