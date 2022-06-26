# 피보나치 함수
import sys


global c0
global c1


def fibonacci(n):
    global c0
    global c1
    if n == 0:
        c0 +=1
        return 0
    elif n == 1:
        c1 +=1 
        return 1
    else: 
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input())
for i in range(n):
    c0 = 0 
    c1 = 0
    fibonacci(int(input()))
    print(c0,c1)