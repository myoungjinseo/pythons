
import sys


n = int(sys.stdin.readline())

l = [[0]*2 for _ in range(n)]

for i in range(n):
    s, e = map(int, sys.stdin.readline().split())
    l[i][0] =s
    l[i][1] =e

l.sort(key = lambda x: (x[1], x[0]))


end_time= l[0][1]
d = 1
for i in range(1,n):
    if end_time <= l[i][0]:
        end_time = l[i][1]
        d += 1

print(d)
