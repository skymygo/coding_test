import sys
K, N = map(int, input().split())
lan = [int(sys.stdin.readline()) for _ in range(K)]
start = 0
end = max(lan)

while start < end:
    mid = (start + end) // 2
    if start == mid:
        mid += 1

    lan_count = sum([_//mid for _ in lan])
    if lan_count >= N:
        start = mid
    elif lan_count < N:
        end = mid-1

print(start)