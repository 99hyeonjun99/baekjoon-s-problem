import sys
input = sys.stdin.readline

n,m=map(int, input().split())
listen_list={}
saw_list=[]

for i in range(0, n):
    listen_list[input().strip()]=i
for i in range(0, m):
    saw_list.append(input().strip())
sorted_saw_list=sorted(saw_list)

count=0
answer_list=[]
for i in sorted_saw_list:
    if i in listen_list:
        count+=1
        answer_list.append(i)
print(count)
for i in answer_list:
    print(i)
