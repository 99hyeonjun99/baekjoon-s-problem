import sys
input = sys.stdin.readline
#종이의 개수
def check(listed, count): #1이면 통과 0이면 실패
    
    checking=1
    for i in range(1, count):
        
        if listed[0]!=listed[i]:
            checking=0
    
    return checking

def add(number): #더하는 함수
    global count1
    global count_1
    global count0
    if number==-1:
        count_1+=1
    elif number==0:
        count0+=1
    elif number==1:
        count1+=1

count1=0
count_1=0
count0=0

def recur(listed, count): #재귀함수
    count_div=count
    count*=count

    if count==1:
        add(listed[0])
    else:
        if check(listed, count)==1:    
            add(listed[0])
        else:
            cnt=0
            for i in range(0,3): #1,2,3  4,5,6  7,8,9 식으로 나눔
                
                div_list1=[]
                div_list2=[]
                div_list3=[]        
                div_num=int(count_div/3)
                for j in range(0,div_num):
                    for k in range(0,div_num):
                        div_list1.append(listed[cnt])
                        cnt+=1
                    for k in range(0,div_num):
                        div_list2.append(listed[cnt])
                        cnt+=1
                    for k in range(0,div_num):
                        div_list3.append(listed[cnt])
                        cnt+=1
       
                if check(div_list1,len(div_list1))==1:
                    add(div_list1[0])
                else:
                    recur(div_list1,div_num)

                if check(div_list2,len(div_list2))==1:
                    add(div_list2[0])
                else:
                    recur(div_list2,div_num)

                if check(div_list3,len(div_list3))==1:
                    add(div_list3[0])
                else:
                    recur(div_list3,div_num)



                   



n=int(input().strip())
listed=[]
for i in range(0, n):
    listed1=list(map(int, input().split()))
    listed+=listed1

recur(listed, n)
print(count_1)
print(count0)
print(count1)

    