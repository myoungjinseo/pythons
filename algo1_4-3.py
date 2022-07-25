# 경우의 수가 많은(예시로 100억 이상) 경우 
n , k = map(int, input().split())
result = 0 

while True:
    # n == k 로 나누어 떨어지는 수가 될 때까지 1씩 빼기
    target = (n//k) * k
    result += (n-target)
    n = target
    # n이 k보다 작을 때(더 이상 나눌 수 없을때) 반복문 탈출
    if n < k:
        break
    result +=1
    n //=k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n-1)
print(result)