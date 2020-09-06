def solution(arr):
  answer = 1
  total_prime_number = dict()
  for i in arr:
    new_prime_number = dict()
    new_i = i
    while new_i > 1:
      th = new_i // 2
      for number in range(1, th + 1):
        if number == 1:
          continue
        if new_i % number == 0:
          if new_prime_number.get(number, 0) == 0:
            new_prime_number[number] = 1
          else:
            new_prime_number[number] += 1
          new_i //= number
          break;
      if th == new_i // 2:
        if new_prime_number.get(new_i, 0) == 0:
          new_prime_number[new_i] = 1
        else:
          new_prime_number[new_i] += 1
        new_i = 1
    for key, value in new_prime_number.items():
      if total_prime_number.get(key, 0) < value:
        total_prime_number[key] = value

  for key, value in total_prime_number.items():
    answer = answer * (key ** value)

  return answer


input_arr = [2,7]
print(solution(input_arr))