#숨바꼭질
#1칸 +- OR 두 배
#count 리스트를 만들고 큐를 만들어 해보기

start=0
last=0
def push(listed, number):
    global last
    
    listed.append(number)
    last+=1
    

def pop(listed):
    global start
    number=listed[start]
    start+=1
    return number

n,m=map(int, input().split())
if n>m:
    print(n-m)
else:
    count=[0 for i in range(10000000)]
    queue=[n]
    number=pop(queue)
    while number!=m:
        if number-1>=0 and count[number-1]==0:
            count[number-1]=count[number]+1
            push(queue,number-1)
        if count[number+1]==0:
            count[number+1]=count[number]+1
            push(queue, number+1)
        if count[2*number]==0 and 2*number<1000000: #범위 벗어남 방지
            count[2*number]=count[number]+1
            push(queue, 2*number)
        number=pop(queue)
    print(count[m])