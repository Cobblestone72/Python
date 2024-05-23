from collections import deque

def solution(maps):
    temp = [[0, 1], [1, 0], [0, -1], [-1, 0]] # 우, 하, 좌, 상
    progress = deque()
    visited = set()
    rows = len(maps)
    cols = len(maps[0])
    unlock = 0

    for i in maps:
        print(i)
    
    for i in range(rows):
        for j in range(cols):
            if maps[i][j] == 'S':
                progress.append((i, j, 0))

    while progress:
        r, c, length = progress.popleft()
        if (r, c) in visited:
            continue
        else:
            visited.add((r, c))
        if maps[r][c] == 'L' and unlock == 0:
            visited.clear()
            progress.clear()
            unlock = 1
        if unlock == 1 and maps[r][c] == 'E':
            return length
        # print(r, c, length)
        # print(progress)
        for dr, dc in temp:
            new_r, new_c = r+dr, c+dc
            if 0 <= new_r < rows and 0 <= new_c < cols and maps[new_r][new_c] != 'X':
                progress.append((new_r, new_c, length+1))

    return -1