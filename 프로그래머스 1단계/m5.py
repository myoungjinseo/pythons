# 수박수박수박수박수?
from re import I


def solution(n):
    answer = '수박' * (n//2)
    answer1  = '수' * (n%2)
    answer =answer + answer1
    return answer
