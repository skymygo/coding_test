def solution(strings, n):
  strings.sort()
  answer = sorted(strings, key=lambda s: s[n])
  return answer

input_a = ["sun", "bed", "car"]
input_n = 1

print(solution(input_a, input_n))