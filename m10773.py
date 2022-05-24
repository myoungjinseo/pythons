k = int(input())

m = []
for i in range(k):
    a = int(input())
    
    if(a == 0):
        del m[-1]
    else:
        m.append(a) 


print(sum(m))