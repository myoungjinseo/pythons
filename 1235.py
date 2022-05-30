n = int(input())
k = [0 for i in range(n)]
for i in range(n):
    k[i] = int(input())
j =10
c = 1 
k1 = set(k[i]%j for i in range(n))
k2 = list(k1)

while(len(k) != len(k2)):
    j*=10
    k1 = set(k[i]%j for i in range(n))
    k2 = list(k1)
    c +=1

print(c)