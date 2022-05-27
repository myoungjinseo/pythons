input_data = input()    #입력값 ex) a1
row = int(input_data[1])    #row = 1
column = int(ord(input_data[0]))-int(ord('a'))+1 # ord = 유니코드 반환 a-a +1 이므로 1

steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)] # 경우의 수
result =0   
for step in steps:  #steps for 문 돌림
    next_row = row + step[0]    # 1+ step[0] for문
    next_column = column + step[1] # 1 + step[1] for 문
    if next_row >=1 and next_row<=8 and next_column >=1 and next_column<=8: # next_row , next_column == 1~8일경우        
        result +=1 #result +1 

print(result)