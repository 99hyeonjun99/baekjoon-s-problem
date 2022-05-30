#수 찾기

#이분탐색 알고리즘 짜기
def binary_search(sorted_list, value):
    low=0
    high=len(sorted_list)-1
    while low<=high:
        mid=int((high+low)/2)
        if sorted_list[mid]>value:
            high=mid-1
        elif sorted_list[mid]<value:
            low=mid+1
        else:
            print("1")
            return
    print('0')
    return



count=int(input())
num_list = list(map(int, input().split()))
sorted_list=sorted(num_list)

count2=int(input())
value_list=list(map(int, input().split()))
for i in range(0, count2):
    binary_search(sorted_list, value_list[i])
