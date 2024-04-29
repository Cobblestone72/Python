def solution(babbling):
    know_word = ["aya", "ye", "woo", "ma"]
    cnt = 0
    for word in babbling:
        for know in know_word:
            word = word.replace(know, " ")
        if not any(c.isalpha() for c in word):
            cnt+=1

    return cnt

print(solution(["aya", "yee", "u", "maa", "wyeoo"]))