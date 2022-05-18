n = int(input())

a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = [b[i] for i in range(n)]
a.sort(reverse=True)
c.sort()

result =0
for i in range(n):
    result += a[i] * c[i]
print(result)