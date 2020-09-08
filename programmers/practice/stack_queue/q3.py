def solution(bridge_length, weight, truck_weights):
    count = 0
    truck_count = 0
    count_weight_list = [0]*1000000
    while truck_count != len(truck_weights):
        count +=1
        if count_weight_list[count] + truck_weights[truck_count] <= weight:
            for i in range(bridge_length):
                count_weight_list[count+i] += truck_weights[truck_count]
            truck_count+=1

    count += bridge_length
    answer = count
    return answer


