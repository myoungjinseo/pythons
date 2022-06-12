import sys


n = int(input())
data = []
for i in range(n):
    data.append(sys.stdin.readline().rstrip())

for i in sorted(data):
    sys.stdout.write(str(i)+'\n')