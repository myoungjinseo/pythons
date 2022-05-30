n = int(input())

m = list(map(int,input().split()))
k =[0 for i in range(n)]
i = 0
j = 0
c1 = 0
while(i != n):
    c = m[i]+1 
    if(c1 != c):
        if k[j] == 0:
            j +=1
            c1 +=1
        else:
            j+=1
    else:
        k[j-1] = i+1
        i += 1
        j = 0
        c1 = 0
for i in range(n):
    print(k[i],end =' ')
