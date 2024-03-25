def solution(plans):
    answer = []
    
    # for name, start, playtime in plans:
    #     print(name, start, playtime)
    plans = sorted(plans, key=lambda x: (x[1]))
    # print("정렬 후--------------------------------------")
    # for name, start, playtime in plans:
    #     print(name, start, playtime)
    for i in range(len(plans)):
        hours, minutes = plans[i][1].split(":")
        plans[i][1] = int(hours)*60 + int(minutes)
        plans[i][2] = int(plans[i][2])
    # for name, start, playtime in plans:
    #     print(name, start, playtime)
    
    later_plans = [[]] # 미뤄둔 plans
    later_plans.pop(0)
    now_plan = [] # 현재 진행중인 과제
    # print("반복 시작--------------------------------------")
    now_plan = plans.pop(0)
    name, start, playtime = now_plan
    
    now_time = start
    while len(plans) > 0 or len(later_plans) > 0:
        name, start, playtime = now_plan
        # print(plans, "///", now_plan, "///", later_plans)
        # print(now_time, int(now_time/60), ":", now_time%60)
        if plans:
            if now_time+playtime > plans[0][1]: # 진행중인 과제가 끝나기 전에 새 과제가 있을 때
                # print("진행중인 과제가 끝나기 전에 새 과제가 있을 때")
                now_plan[2] = playtime - plans[0][1] + now_time
                later_plans.append(now_plan)
                now_time += plans[0][1] - now_time
                now_plan = plans.pop(0)
        
            else: # 진행중인 과제가 끝났을 때
                # print("진행중인 과제가 끝났을 때 {0}".format(name))
                answer.append(name) # 끝난 과제 answer에 추가
                now_time += playtime

                if plans[0][1] == now_time: # 새로운 과제가 즉시 시작해야 한다면
                    # print("새로운 과제가 먼저 시작해야 한다면")
                    now_plan = plans.pop(0)

                elif not later_plans: # 미뤄둔 과제가 없다면
                    now_time = plans[0][1]
                    now_plan = plans.pop(0)

                else: # 미뤄둔 과제가 먼저 시작해야 한다면
                    # print("미뤄둔 과제가 먼저 시작해야 한다면")
                    now_plan = later_plans.pop()
        else:
            answer.append(name)
            now_plan = later_plans.pop()
    #     print("------------------------------")
    
    # print(plans, "///", now_plan, "///", later_plans)
    answer.append(now_plan[0])

    return answer

# 변수
# * 새로운 과제, 미뤄둔 과제, 진행중인 과제
# 1. 새로운 과제는 과제 진행중에 스틸 가능
# 2. 미뤄둔 과제는 과제 진행중에 스틸 불가능
# 3. 과제를 마쳤는데 새로운 과제가 시작할 시간이 아니면 미뤄둔 과제 시작

# print(solution([["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]))
# print(solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]))
# print(solution([["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]]))
# print(solution([["aaa", "12:50", "1"], ["bbb", "0:0", "100"], ["ccc", "23:59", "100"]]))
# print(solution([["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]]))
# print(solution([["aaa", "10:00", "30"], ["bbb", "11:00", "30"], ["ccc", "12:00", "30"]])) # 모든 과제의 시작 시간이 현재 시간보다 이전인 경우
# print(solution([["aaa", "12:00", "20"], ["bbb", "12:30", "30"], ["ccc", "13:00", "10"]])) # 미뤄둔 과제가 끝나고 바로 시작해야 하는 새로운 과제가 있을 경우
# print(solution([["a", "00:00", "1"], ["b", "00:01", "100"], ["c", "00:02", "100"], ["d", "00:03", "1"], ["e", "00:04", "100"], ["f", "00:05", "100"], ["g", "00:06", "100"]]))
print(solution([["a","09:00","30"],["b","09:10","20"],["c","09:15","20"],["d","09:55","10"],["e","10:50","5"]]))
