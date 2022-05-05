# my conding 10분 소요 
from difflib import restore


m,n  = map(int,input().split())

result = 0
for i in range(m):
    data = list(map(int,input().split()))
    a = min(data)
    result = max(result, a)
print(result)

#정답1 
# n,m = map(int,input().split())

# result = 0
# for i in range(n):
#     data = list(map(int,input().split()))
#     min_value =min(data)
#     result = max(result,min_value)
# print(result)

#정답2 
# n,m = map(int,input().split())
# result =0
# for i in range(n):
#     data = list(map(int,input().split()))
#     min_value = 10001
#     for a in data:
#         min_value = min((min_value,a))
#     result = max(result,min_value)
# print(result)