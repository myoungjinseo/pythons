#서울에서 김서방 찾기
def solution(seoul):
    answer = ''
    i = 0
    while seoul[i] not in 'Kim':
        i += 1
    answer = f'김서방은 {i}에 있다'
    return answer