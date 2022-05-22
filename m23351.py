n,k,a,b = map(int,input().split(" "))

data = [int(k) for i in range(n)]

count =0
j = 0

while(0 not in data):
    for i in range(a):
        data[j%n] += b
        j +=1
    for i in range(n):
        data[i] -= 1
    count +=1
print(count)
