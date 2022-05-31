n = int(input())

data = [0 for i in range(n)]

data = list(map(int,input().split()))
data.sort()

for i in range(1,n):
    data[i] = data[i] + data[i-1]

print(sum(data))
