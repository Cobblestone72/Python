def count_O(matrix):
    count = 0
    for row in matrix:
        for element in row:
            if element == 'O':
                count += 1
    return count

def count_X(matrix):
    count = 0
    for row in matrix:
        for element in row:
            if element == 'X':
                count += 1
    return count

def line_check(board):
    X_clear = 0
    O_clear = 0
    
    # 모든 검사할 라인의 조건을 리스트에 담기
    checks = [
        (board[0][0], board[0][1], board[0][2]),
        (board[1][0], board[1][1], board[1][2]),
        (board[2][0], board[2][1], board[2][2]),
        (board[0][0], board[1][0], board[2][0]),
        (board[0][1], board[1][1], board[2][1]),
        (board[0][2], board[1][2], board[2][2]),
        (board[0][0], board[1][1], board[2][2]),
        (board[0][2], board[1][1], board[2][0])
    ]
    
    # 리스트를 순회하며 조건 검사
    for a, b, c in checks:
        if a == b == c:
            if a == 'O':
                O_clear = 1
            elif a == 'X':
                X_clear = 1
    
    return O_clear, X_clear

def solution(board):
    answer = 1
    for i in board:
        print(i)
    print(count_O(board))
    print(count_X(board))
    cntO = count_O(board)
    cntX = count_X(board)
    O_clear, X_clear = line_check(board)
    # 1. O가 먼저 시작해야함 (O가 없는데 X가 있으면 안됨)
    # 2. O와 X는 번갈아서 둬야함 (O와 X가 2개 이상 차이나면 안됨)
    # 3. 한쪽이 이어서 3개를 놓으면 게임이 끝나고 더이상 둘 수 없음 (O가 완성되어있으면 X는 O의 개수보다 1개 적어야함
    #                                                        X가 완성되어있으면 O는 X의 개수와 같아야함)
    
    if cntO == 0 and cntX > 0:
        return 0
    elif abs(cntO - cntX) > 1:
        return 0
    elif O_clear and cntX != cntO-1 or X_clear and cntO != cntX:
        return 0
    
    print(O_clear, X_clear)
    return answer