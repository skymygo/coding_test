def solution(phone_book):
    answer = True
    phone_book = sorted(phone_book, key=lambda pb : len(pb))

    for i in range(len(phone_book)):
        for j in range(i+1, len(phone_book)):
            if phone_book[j].startswith(phone_book[i]):
                print(phone_book[i], phone_book[j])
                return False
    return True

print(solution(['123','456','789']))