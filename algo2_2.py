n = int(input())

c = 0
for i in range(n+1):    
    for j in range(60):
        for k in range(60):
            if('3' in str(i)+str(j)+str(k)):
                c +=1
print(c)
