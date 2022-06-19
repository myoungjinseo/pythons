from tkinter import X
# 음양구하기

def solution(absolutes, signs):
    answer = 0
    for i in range(len(signs)):
        if signs[i] != True:
            answer += (absolutes[i] * -1)
        else:
            answer += absolutes[i]
    return answer
absolutes = []
signs = []
absolutes = list(map(int, input().split(",")))
signs = list(map(lambda x: x == "true",input().split(",")))

print(solution(absolutes,signs))
