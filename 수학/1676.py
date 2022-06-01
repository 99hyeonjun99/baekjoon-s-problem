#팩토리얼 0의 개수 구하기

n=int(input())
ans=1
count=0
for i in range(n,0,-1):
    div=i
    while div%5==0:
        count+=1
        div/=5


print(count)