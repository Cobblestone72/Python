from collections import deque

def solution(board):
    answer = 0
    temp = [[-1, 0],
            [0, 1],
            [1 , 0],
            [0 , -1]]
    progress = deque()
    progress_wait = deque()
    arrived = []
    rows = len(board)
    cols = len(board[0])

    # for i in board:
    #     print(i)

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'R':
                progress.append((i, j))
                break
        if board[i][j] == 'R':
            break
    
    while progress:
        # print("-----------------------------------------")
        # print("answer:", answer)
        end_point = progress.popleft()
        if board[end_point[0]][end_point[1]] == 'G':
            return answer
        # board[end_point[0]] = list(board[end_point[0]])
        # board[end_point[0]][end_point[1]] = 'S'
        # board[end_point[0]] = ''.join(board[end_point[0]])
        if end_point in arrived:
            if not progress:
                progress.extend(progress_wait)
                progress_wait.clear()
                answer += 1
            continue
        else:
            arrived.append(end_point)
        # for i in board:
        #     print(i)
        # print(end_point)
        for dx, dy in temp:
            temp_x = end_point[0] + dx
            temp_y = end_point[1] + dy
            if 0 <= temp_x < rows and 0 <= temp_y < cols and (board[temp_x][temp_y] == '.' or board[temp_x][temp_y] == 'G'):
                # print("dx, dy, temp_x, temp_y:", dx, dy, "//", temp_x, temp_y)
                while True:
                    temp_x += dx
                    temp_y += dy
                    if 0 > temp_x or temp_x >= rows or 0 > temp_y or temp_y >= cols or board[temp_x][temp_y] == 'D':
                        progress_wait.append((temp_x - dx, temp_y - dy))
                        break
        # print("progress:", progress, "progress_wait:", progress_wait)
        if not progress:
            progress.extend(progress_wait)
            progress_wait.clear()
            answer += 1
    return -1

# print(solution(["...D..R",
#                 ".D.G...",
#                 "....D.D",
#                 "D....D.",
#                 "..D...."]))
print(solution(["..R",
                "...",
                "...",
                "..D",
                "DG."]))