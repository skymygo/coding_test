def solution(priorities, location):
    answer = 0

    location_value = priorities[location]
    new_location = location
    for i in range(location):
        if priorities[i] < location_value:
            new_location -= 1
    location = new_location
    priorities = [i for i in priorities if i >= location_value]
    priorities_sort = sorted(priorities, reverse=True)
    i = 0

    while location_value != priorities_sort[i]:
        index = priorities.index(priorities_sort[i])

        priorities = priorities[index+1:] + priorities[:index]
        if location < index:
            location += len(priorities) - index
        else:
            location -= (1 + index)
        i += 1
    answer = i + location+1
    return answer