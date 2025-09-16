import sys
K, N = map(int, input().split())
numbers = input().split(" ")
numbers = [ int(n) for n in numbers ]

_nset = {_ for _ in numbers if _ != 0}
_nlist = [ _ for _ in numbers]
s_q = list()
if _nlist[0] == 0:
    for n in range(1, K+1):
        if n not in _nset:
            __nset = {_ for _ in numbers  if _ != 0}
            __nset.add(n)
            __nlist = [_ for _ in _nlist]
            __nlist[0] = n
            s_q.append( (0,0,__nset, __nlist))
else:
    s_q.append((0, 0, _nset, _nlist))

s_count = 0

while s_q:
    pos, score, _nset, _nlist = s_q.pop(0)
    for _ in _nlist[:pos]:
        if _ < _nlist[pos]:
            score = score + 1

    if score > N:
        continue

    pos += 1
    if pos == K:
        if score == N:
            s_count += 1
        continue


    if _nlist[pos] == 0:
        for n in range(1,K+1):
            if n not in _nset:
                __nset = {_ for _ in _nset}
                __nset.add(n)
                __nlist = [_ for _ in _nlist]
                __nlist[pos] = n
                s_q.append((pos, score, __nset, __nlist))
    else:
        s_q.append((pos, score, _nset, _nlist))

print(s_count)