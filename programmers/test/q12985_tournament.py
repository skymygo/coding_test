class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree():
    def __init__(self):
        self.head = None

    def push(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        cur_node = self.head
        while True:
            if value < cur_node.value:
                if cur_node.left:
                    cur_node = cur_node.left
                else:
                    cur_node.left = Node(value)
                    return
            else:
                if cur_node.right:
                    cur_node = cur_node.right
                else:
                    cur_node.right = Node(value)
                    return

    def get_path(self, value):
        cur_node = self.head

        path = []
        while cur_node and cur_node.value != value:
            path.append(cur_node.value)
            if value < cur_node.value:
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right

        return path


def solution_1(n, a, b):
    answer = 0

    players = [_ + 1 for _ in range(n)]
    stack = [players]
    tree = Tree()

    while stack:
        cur_data = stack.pop()
        tree.push((cur_data[0] + cur_data[-1]) / 2)
        if len(cur_data) > 3:
            stack.append(cur_data[0:len(cur_data) // 2])
            stack.append(cur_data[len(cur_data) // 2:])

    a_path = tree.get_path(a)
    b_path = tree.get_path(b)

    for i in range(len(a_path) - 1, -1, -1):
        answer += 1
        if a_path[i] == b_path[i]:
            return answer

    return answer


def solution(n, a, b):
    answer = 1
    players_queue = [[_ + 1 for _ in range(n)]]
    while True:
        players = players_queue.pop()
        if a in players and b in players:
            players_queue += [players[:len(players) // 2], players[len(players) // 2:]]
        elif a not in players and b not in players:
            continue
        else:
            break

    player_count = len(players)
    while player_count > 1:
        answer += 1
        player_count /= 2

    return answer


print(solution(8, 4, 7))
