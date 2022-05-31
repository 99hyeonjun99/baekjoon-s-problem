# 구현 빨라지기 위해 사용
import sys
input = sys.stdin.readline

count=int(input())
#2차배열을 만들기 위해 자리를 0으로 채움
num_list=[0 for i in range(count)]
#입력
for i in range(count):
    num_list[i]=list(map(int, input().split()))

#정렬함수 사용
sorted_list=sorted(num_list,key=lambda x:(x[1], x[0]))
for i in range(count):
    print(sorted_list[i][0], sorted_list[i][1])