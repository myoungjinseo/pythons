# 숫자 카드 게임 
# n, m 의 행렬 개수 
# 각 행마다 가장 작은 수를 찾은 뒤에 그 수 중에서 가장 큰수를 찾는 게임
# min() 함수를 이용한 답안

n, m = map(int, input().split())

result = 0 
# 한줄씩 데이터 입력받기
for i in range(n):
    data = list(map(int,input().split()))
    min_value = min(data)   # 현재 줄에서 가장 작은 수 찾기  
    result = max(result,min_value)  # 가장 작은 수 중에서 가장 큰 수 찾기

print(result)