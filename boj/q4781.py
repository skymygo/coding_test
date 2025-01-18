import sys

if __name__ == "__main__":
    _lines = []
    while True:
        _lines.append(sys.stdin.readline().rstrip())
        if(_lines[-1] == '0 0.00'):
            break

    cur_pos = 0
    while _lines[cur_pos] != '0 0.00':
        candy_count, money = _lines[cur_pos].split(' ')
        cur_pos += 1
        money = int(float(money) * 100 +0.5)
        calorie = [0] * (int(money)+1)
        candies = []
        for i in range(int(candy_count)):
            candy_cal, candy_price = _lines[cur_pos].split(' ')
            cur_pos+=1
            candies.append((int(candy_cal), int(float(candy_price) * 100 + 0.5)))
        for i in range(len(calorie)):
            cur_cal = [0]
            for c in candies:
                if i >= c[1]:
                    cur_cal.append(calorie[i-int(c[1])] + c[0])
            calorie[i] = max(cur_cal)

        print(max(calorie))