# 성적이 낮은 순서로 학생 출력하기

n = int(input())

array = []
for i in range(n):
    data = input().split()
    array.append((data[0], int(data[1])))

# 키를 이용하여 lambda식으로 이용해서 점수로 정렬 
array.sort(key=lambda student: student[1])

for student in array:
    print(student[0], end=' ')