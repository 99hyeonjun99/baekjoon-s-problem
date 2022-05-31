import sys
input = sys.stdin.readline

count1,count2=map(int, input().split())
my_dict={}
my_dict1={}
for i in range(0,count1):
    inp_str=input().strip()
  
    my_dict[inp_str]=i+1
    my_dict1[i+1]=inp_str


for i in range(0, count2):
    vari=input().strip()
    if vari.isnumeric()==True:
        vari_int=int(vari)
        print(my_dict1[vari_int])
    else:
        print(my_dict[vari])