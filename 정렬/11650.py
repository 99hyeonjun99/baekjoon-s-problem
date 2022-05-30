# 구현 빨라지기 위해 사용
import sys
input = sys.stdin.readline

count=int(input())
num_list=[0 for i in range(count)]
for i in range(count):
    num_list[i]=list(map(int, input().split()))

sorted_list=sorted(num_list)
for i in range(count):
    print(sorted_list[i][0], sorted_list[i][1])