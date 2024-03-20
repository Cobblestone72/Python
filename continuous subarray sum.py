# def solution(sequence, k):
#     answer = []

#     for i in range(len(sequence)):
#         sum = 0
#         for j in range(i, len(sequence)):
#             sum += sequence[j]
#             if sum >= k:
#                 if sum == k:
#                     answer.append((i, j))
#                 break
    
#     answer = sorted(answer, key=lambda x: (x[1] - x[0], x[0]))
    
#     return list(answer[0])

# 테스트 6, 8~17, 24~30 시간 초과
# 중첩 for문 완전 탐색 때문이라고 추측됨
# -----------------------------------------------------

# def solution(sequence, k):
#     answer = []

#     for i in range(len(sequence)):
#         if sequence[i] == k:
#             return (i, i)

#     for length in range(2, len(sequence)+1): # 탐색할 길이 (2 ~ sequence의 길이)
#         i = 0 # 탐색을 시작할 인덱스 (0 ~ k/length보다 같거나 작고 sequence의 길이보다 같거나 작을때만 반복)
#         while i <= k/length and i < len(sequence)-length+1: # 시작 인덱스가 k/length보다 같거나 작고 끝 인덱스가 sequence의 길이를 넘지 않도록 반복
#             sum = 0 # 범위의 합
#             for j in range(i, i+length): # 시작 인덱스부터 length만큼 다 더한다
#                 print("length:", length, ", i:", i, ", j:", j, ", k/length:", k/length)
#                 sum += sequence[j]
#                 if k <= sum:
#                     # print(sum)
#                     if k == sum:
#                         return (i, j)
#                     break
#             i += 1

# 실패 + 시간초과
# 분명 밑에 실행한것들은 다 되는데 문제가 심각하다
# 이 코드에 대한 자문을 얻던 중 투포인터라는 것을 알아내었다
# -----------------------------------------------------

def solution(sequence, k):
    answer = []

    prefix_sum = [0] * len(sequence)
    prefix_sum[0] = sequence[0]
    # [0] ~ [len(sequence)]까지의 누적합 구하기
    for i in range(1, len(sequence)):
        prefix_sum[i] = prefix_sum[i-1] + sequence[i]
    print(prefix_sum)

    e = 0
    for s in range(len(sequence)):
        part_sum = 0
        while part_sum < k and e < len(sequence):
            # s부터 e까지의 부분합 구하기
            if s-1 < 0:
                part_sum = prefix_sum[e]
            else:
                part_sum = prefix_sum[e] - prefix_sum[s-1]
            print(f"{part_sum} = {s, e})")
            e += 1
        if part_sum == k:
            print(f"answer.append({(s, e-1)})")
            answer.append((s, e-1))
        e -= 1
    
    answer = sorted(answer, key=lambda x: (x[1] - x[0], x[0]))
    print(answer)
    return list(answer[0])

# print(subtotal([1, 2, 3, 4, 5], 1, 2))

# print(solution([1, 2, 3, 4, 5], 7)) # [2, 3]
print(solution([1, 1, 1, 2, 3, 4, 5], 5)) # [6, 6]
# print(solution([2, 2, 2, 2, 2], 6)) # [0, 2]
# print(solution([1, 1, 5, 6, 7], 12)) # [1, 3]
# print(solution([1, 1, 5, 6, 7, 7, 50, 50, 50, 100, 100, 100, 1000], 150)) # [8, 9]
# print(solution([1, 1, 5, 6, 7], 20)) # [0, 4]
# print(solution([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144], 52)) # [2, 7]
# print(solution([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 10)) # [0, 9]
# print(solution([1, 2, 3, 4, 5], 6))
# print(solution([1, 1, 1, 1, 1], 2))