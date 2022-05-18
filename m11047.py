n,k = map(int,input().split(" "))

c = [int(input()) for i in range(n)]
    
cnt = 0
for i in reversed(range(n)):
    cnt += k//c[i]
    k = k%c[i]

print(cnt)