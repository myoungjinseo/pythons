# EX R R R U D D 를 받았을 경우
n = int(input()) # n*n 정사각형
x,y = 1,1   # 1,1 에서 시작
plans = input().split()     # 이동할 방향 입력 

dx= [0,0,-1,1]  
dy =[-1,1,0,0]
move_types = ['L','R','U','D']

for plan in plans:  # plan = R R R U D D
    for i in range(len(move_types)):    #i = 0~3
        if plan == move_types[i]:   # plan(R R R U D D 순) == i(0~3 돌아가고) 
            nx = x +dx[i]       # R 일 경우 i =1 dx = 0 dy =1 
            ny = y +dy[i]       # nx, ny = 1, 2
    if nx <1 or ny <1 or nx>n or ny >n :   # nx or ny 0이거나 n(입력문) 보다 클 때 
        continue

    x,y = nx,ny

print(x,y)