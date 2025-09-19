from itertools import product
import copy


def rotate_clock(matrix, x, y):
    """
    (x, y) 위치의 시계를 회전하면 해당 시계와 인접한 시계들도 함께 회전한다.
    """
    n = len(matrix)
    matrix[x][y] = (matrix[x][y] + 1) % 4
    if x > 0:
        matrix[x - 1][y] = (matrix[x - 1][y] + 1) % 4
    if x < n - 1:
        matrix[x + 1][y] = (matrix[x + 1][y] + 1) % 4
    if y > 0:
        matrix[x][y - 1] = (matrix[x][y - 1] + 1) % 4
    if y < n - 1:
        matrix[x][y + 1] = (matrix[x][y + 1] + 1) % 4


def count_moves(clockHands, first_row_moves):
    """
    주어진 첫 번째 행의 조작(first_row_moves)에 대해 나머지 행들을 해결하며 최소 조작 횟수를 계산한다.
    """
    n = len(clockHands)
    matrix = copy.deepcopy(clockHands)
    moves = 0

    # 첫 번째 행 처리
    for y in range(n):
        for _ in range(first_row_moves[y]):
            rotate_clock(matrix, 0, y)
            moves += 1

    # 아래 행들 처리
    for x in range(1, n):
        for y in range(n):
            # 위쪽 행이 12시 방향이 아니면 현재 시계를 돌려야 함
            if matrix[x - 1][y] != 0:
                rotations = (4 - matrix[x - 1][y]) % 4
                for _ in range(rotations):
                    rotate_clock(matrix, x, y)
                    moves += 1

    # 마지막 행이 전부 12시인지 확인
    if all(matrix[n - 1][y] == 0 for y in range(n)):
        return moves
    return float('inf')


def solution(clockHands):
    n = len(clockHands)
    min_moves = float('inf')

    # 첫 번째 행을 0~3번 회전하는 모든 경우의 수를 시도
    for first_row_moves in product(range(4), repeat=n):
        min_moves = min(min_moves, count_moves(clockHands, first_row_moves))

    return min_moves
