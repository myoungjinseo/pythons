# 없는 숫자 더하기
def solution(numbers):
    answer = 0
    a = {1,2,3,4,5,6,7,8,9}
    for i in numbers:   # 들어오는 숫자를 a에서 제거
        if i in a:
            a.remove(i)
    for i in a:     # a 값을 다 더해줌
        answer += i
    return answer
numbers = {1,2,3,4,5,6}
print(solution(numbers))

# 문제 답안보고 후기 
# in을 이용하지 않고 not in을 이용하면 더 편하게 계산 가능할것 같다.