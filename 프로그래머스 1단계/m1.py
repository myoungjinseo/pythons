# 숫자 문자열과 영단어
def solution(s):
    a = ['zero','one','two','three','four','five','six','seven','eight','nine']     # 영어 
    b = ['0','1','2','3','4','5','6','7','8','9']   #숫자
    i = 0   
    for i in range(10):
        if s.find(a[i]) >=0:    # 영어 발견시 
            s = s.replace(a[i],b[i])    # 숫자로 바꿔준다
    
            
    answer = int(s)
    return answer

s = input()
print(solution(s))