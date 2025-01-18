def sqrt(n: int, tolerance: float = 1e-15):
    estimate = n
    while True:
        new_estimate = (estimate + (n / estimate)) / 2
        if abs(new_estimate - estimate) < tolerance:
            return new_estimate
        estimate = new_estimate


def is_prime(n: int):
    last_number = int(sqrt(n))
    for i in range(2, last_number + 1):
        if n % i == 0:
            return False
    return True


def primes(arr: list[int]):
    res = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            for k in range(j + 1, len(arr)):
                sum_num = arr[i] + arr[j] + arr[k]
                if is_prime(arr[i] + arr[j] + arr[k]):
                    print(sum_num, arr[i], arr[j], arr[k])
                    res += 1
    return res


print(primes([_ for _ in range(1,10)]))
