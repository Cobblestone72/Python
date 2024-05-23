# 실패작

use_end_point = []
answer = -1

def find_access(board, end_point, cnt):
    global answer
    cnt += 1
    temp = [[-1, 0],
            [0, 1],
            [1 , 0],
            [0 , -1]]

    if board[end_point[0]][end_point[1]] == 'R':
        return 1

    # board[end_point[0]] = list(board[end_point[0]])
    # board[end_point[0]][end_point[1]] = 'S'
    # board[end_point[0]] = ''.join(board[end_point[0]])
    # for i in board:
    #     print(i)
    # print("end_point:", end_point, "cnt:", cnt)
    # print("----------------------------------")

    if end_point in use_end_point:
        # board[end_point[0]] = list(board[end_point[0]])
        # board[end_point[0]][end_point[1]] = '.'
        # board[end_point[0]] = ''.join(board[end_point[0]])
        return 0
    else:
        use_end_point.append(end_point)

    rows = len(board)
    cols = len(board[0])
    
    for dx, dy in temp:
        new_x = end_point[0] + dx
        new_y = end_point[1] + dy
        # print("========================================")
        # print("========================================")
        # print("new_x, new_y:", [new_x, new_y])

        board_temp = '보드 바깥'
        if 0 <= new_x < rows and 0 <= new_y < cols:
            board_temp = board[new_x][new_y]
        # print('board_temp:', board_temp, " y:", new_x, " x:", new_y)
        if board_temp == 'D' or board_temp == '보드 바깥':
            # print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            # print("temp_point:", [new_x, new_y])
            j = -1

            while 0 <= end_point[0] + dx * j < rows and 0 <= end_point[1] + dy * j < cols and board[end_point[0] + dx * j][end_point[1] + dy * j] != 'D':
                # if 0 <= end_point[0] + dy + dx * j < rows and 0 <= end_point[1] + dx + dy * j < cols:
                #     print("next side1_point:", [end_point[0] + dy + dx * j, end_point[1] + dx + dy * j])
                #     print("next side1_temp:", board[end_point[0] + dy + dx * j][end_point[1] + dx + dy * j])

                # print("next temp_point:", [end_point[0] + dx * j, end_point[1] + dy * j])
                # print("next board_temp:", board[end_point[0] + dx * j][end_point[1] + dy * j])

                # if 0 <= end_point[0] - dy + dx * j < rows and 0 <= end_point[1] - dx + dy * j < cols:
                #     print("next side2_point:", [end_point[0] - dy + dx * j, end_point[1] - dx + dy * j])
                #     print("next side2_temp:", board[end_point[0] - dy + dx * j][end_point[1] - dx + dy * j])
                
                # 이 과정에서 옆부분이 보드 바깥이거나 D면 그 부분을 다시 돌림 *재귀함수
                if 0 > end_point[0] + dy + dx * j or end_point[0] + dy + dx * j >= rows or 0 > end_point[1] + dx + dy * j or end_point[1] + dx + dy * j >= cols or board[end_point[0] + dy + dx * j][end_point[1] + dx + dy * j] == 'D'\
                    or 0 > end_point[0] - dy + dx * j or end_point[0] - dy + dx * j >= rows or 0 > end_point[1] - dx + dy * j or end_point[1] - dx + dy * j >= cols or board[end_point[0] - dy + dx * j][end_point[1] - dx + dy * j] == 'D': 
                    # board[end_point[0]] = list(board[end_point[0]])
                    # board[end_point[0]][end_point[1]] = '.'
                    # board[end_point[0]] = ''.join(board[end_point[0]])

                    num = find_access(board, [end_point[0] + dx * j, end_point[1] + dy * j], cnt)
                    if num == 1:
                        # print("정답이야")
                        if answer > cnt or answer == -1:
                            answer = cnt

                # print("---------------------------")
                j -= 1
    
    # board[end_point[0]] = list(board[end_point[0]])
    # board[end_point[0]][end_point[1]] = '.'
    # board[end_point[0]] = ''.join(board[end_point[0]])
    return answer

def solution(board):

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'G':
                end_point = [i, j]
                board[i] = list(board[i])
                board[i][j] = 'S'
                board[i] = ''.join(board[i])
                break
        if board[i][j] == 'S':
            break
    
    return find_access(board, end_point, 0)

# print(solution(["......R",
#                 ".DDDDDD",
#                 ".......",
#                 "DDDDDD.",
#                 "G......"]))
print(solution(["..R",
                "...",
                "...",
                "..D",
                "DG."]))
# print(solution(["GD.D..R",
#                 ".D.....",
#                 "....D.D",
#                 "D....D.",
#                 "..D...."]))
# print(solution([".D.R",
#                 "....",
#                 ".G..",
#                 "...D"])) # 도착지점 근처에 벽이 없음