def solution(spell, dic):
    for word in dic: # 단어를 가져온다
        sp_temp = spell[:] # spell을 복사해서 sp_temp에 넣는다
        for abc in word: # 단어의 알파벳을 가져온다
            for item in sp_temp: # sp_temp의 아이템을 가져온다
                if item == abc: # sp_temp에 해당하는 알파벳이 있다면
                    sp_temp.remove(item) # 그 알파벳을 sp_temp에서 제거한다
        if not sp_temp: # 만약 모든 알파벳을 사용했다면
            return 1 # 1을 리턴한다
    return 2 # 모두 검사해봤을때 모든 알파벳을 사용한게 없다면 2를 리턴한다

# 가져온 코드 (set 활용)
# def solution(spell, dic):
#     spell = set(spell)
#     # 어짜피 있는지 없는지만 확인하면 되니 set을 통해 중복을 제거한다
#     for s in dic:
#         if not spell-set(s): # 두 집합을 빼서 남은게 없다면 1을 리턴한다
#             # 이 경우 ["p", "o", "s"]일때 poos라는 단어에도 1을 리턴한다
#             return 1
#     return 2

print(solution(["p", "o", "s"], ["sod", "eocd", "qixm", "adio", "soo", "poos"]))
print(solution(["z", "d", "x"], ["def", "dww", "dzx", "loveaw"]))