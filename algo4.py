# my conding 10분 소요

n,k = map(int,input().split())

count = 0
while(n != 1):

    if(n%k == 0):
        n = n/k
        count +=1
    else:
        count +=1
        n -= 1 
print(count)

# 정답1
# n,k =  map(int, input().split())

# result =0

# while n>=k:
#     while n%k !=0:
#         n -=1
#         result +=1 
#     n //= k
#     result += 1
# while n>1:
#     n-=1
#     result +=1

# print(result)

# 정답2
# n,k = map(int,input().split())
# result = 0
# while True:
#     target = (n//k)*k
#     result += (n - target)
#     n = target
#     if n < k:
#         break
#     result += 1
#     n //= k

# result += (n-1)
# print(result)