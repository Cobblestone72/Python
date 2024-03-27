def mine(picks, minerals):
    cnt = 5
    tired_sum = 0
    while minerals:
        if cnt == 5:
            if not picks: break
            now_pick = picks.pop(0)
            if now_pick == "diamond": tired = [1, 1, 1]
            elif now_pick == "iron": tired = [5, 1, 1]
            else: tired = [25, 5, 1]
            cnt = 0
        
        if minerals[0] == "diamond": tired_sum += tired[0]
        elif minerals[0] == "iron": tired_sum += tired[1]
        else: tired_sum += tired[2]
        minerals.pop(0)
        
        cnt += 1
    return tired_sum

def solution(picks, minerals):

    # new_picks 리스트에 "diamond", "iron", "stone"으로 순서대로 넣기
    # 효율적으로 뭘 넣어야할지 판단
    # 앞에서부터 5개씩 나눠서 다이아 25, 철 5, 돌 1로 합계내기
    mmminerals = minerals[:]
    cnt_minerals = {}
    i = 0

    while len(mmminerals) > 4 and i < sum(picks):
        cnt = 0
        for _ in range(5):
            now_minerals = mmminerals.pop(0)
            if now_minerals == "diamond": cnt += 25
            elif now_minerals == "iron": cnt += 5
            else: cnt += 1
            print("now_minerals = {0}".format(now_minerals))
            print("cnt = {0}".format(cnt))

        cnt_minerals[i] = cnt
        print(f"cnt_minerals[{i}] = {cnt}")
        i += 1
    cnt = 0
    print(mmminerals, picks, i)
    if i < sum(picks):
        for _ in range(len(mmminerals)):
            now_minerals = mmminerals.pop(0)
            if now_minerals == "diamond": cnt += 25
            elif now_minerals == "iron": cnt += 5
            else: cnt += 1
        cnt_minerals[i] = cnt
        print(f"cnt_minerals[{i}] = {cnt}")
    print(cnt_minerals)

    print("합계가 높은 거부터 정렬")
    # 합계가 높은 거부터 정렬
    cnt_minerals = dict(sorted(cnt_minerals.items(), key=lambda item: item[1], reverse=True))
    print(cnt_minerals)

    # 다이아, 철, 돌 순으로 넣기
    for i in cnt_minerals.items():
        if not picks: break
        if picks[0] > 0:
            cnt_minerals[i[0]] = "diamond"
            picks[0] -= 1
        elif picks[1] > 0:
            cnt_minerals[i[0]] = "iron"
            picks[1] -= 1
        else:
            cnt_minerals[i[0]] = "stone"
            picks[2] -= 1
        print(i[1])
    print(cnt_minerals)

    cnt_minerals = dict(sorted(cnt_minerals.items(), key=lambda item: item[0]))
    print(cnt_minerals)

    new_picks = list(cnt_minerals.values())
    
    print(new_picks, minerals)
    return mine(new_picks, minerals)

# print(solution([1, 3, 2], ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"])) # 12
# print(solution([1, 0, 1], ["iron", "iron", "iron", "iron", "diamond", "diamond", "diamond"])) # 47
# print(solution([0, 1, 1], ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"])) # 50
# print(solution([1, 1, 1], ["stone", "stone", "stone", "stone", "stone", "diamond", "diamond", "diamond", "diamond", "diamond", "stone", "stone", "stone", "stone"])) # 14
# print(solution([1, 1, 0], ["iron", "iron", "diamond", "iron", "stone", "diamond", "diamond", "diamond"])) # 12
print(solution([0, 1, 99], ["diamond", "diamond", "diamond", "diamond", "diamond", "diamond"])) # 50
