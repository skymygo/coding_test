import sys

target_list = []

while True:
    _ = int(sys.stdin.readline())
    if _ == 0:
        break
    target_list.append(_)

for i in target_list:
    path_sum = [1, 2]
    for j in range(2, i):
        path_sum.append(path_sum[-1] + path_sum[-2])
    if i == 1:
        print(path_sum[0])
        continue
    print(path_sum[-1])
