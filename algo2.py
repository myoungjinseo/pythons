# my conding 15분 소요 
N,M,K = map(int,input().split( ))
data = list(map(int,input().split( )))
e = 0
c = 0
data.sort()
e = M / (K+1) 
c = data[N-1] * K + data[N-2]
result = c*e +M%(K+1)*c
print(result)

# 정답 코드
# n,m,k = map(int,input().split())
# data = list(map(int,input().split()))

# data.sort()
# first = data[n-1] #첫번째 큰수
# second = data[n-2] # 두번째 큰수

# result = 0

# while True:  
#     for i in range(k): 
#         if m == 0:  
#             break
#         result +=first
#         m -=1 
#     if m == 0:
#         break
#     result += second
#     m -=1
# print(result)

#정답2 
# n,m,k = map(int,input().split())
# data = list(map(int,input().split()))

# data.sort()
# first = data[n-1]
# second = data[n-2]

# count = int(m/(k+1)) *K
# count += m%(k+1)

# result =0
# result += (count) *first
# result += (m-count) * second


# print(result)
