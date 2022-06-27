# 문자열 내림차순으로 배치하기 
def solution(s):
    answer = ''
    w = list(s)
    w.sort(reverse = True)
    for i in range(len(w)):
        answer += w[i]
    return answer