def solution(tickets):
    tickets = sorted(tickets, key=lambda x : x[1])
    ticket_queue = [['ICN', tickets, ['ICN']]]
    while( len(ticket_queue) > 0):
        start, _tickets, routes = ticket_queue[0]
        del ticket_queue[0]
        for pos in range(len(_tickets)):
            if _tickets[pos][0] == start:
                _copy_tickets = _tickets.copy()
                end = _tickets[pos][1]
                del _copy_tickets[pos]
                if len(_copy_tickets) == 0: return routes  + [end]
                ticket_queue.append([end, _copy_tickets, routes.copy() + [end]])
    answer = []
    return answer

if __name__ == '__main__':
    input = [[["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]], [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]]
    output = [["ICN", "JFK", "HND", "IAD"], ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]]

    for _input, _output in zip(input, output):
        pred = solution(_input)
        print('[{}]\tinput: {}\toutput: {}\tpred: {}'.format(pred == _output, _input, _output, pred))