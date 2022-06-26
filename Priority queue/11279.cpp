#include <iostream>
#include <cstring>
using namespace std;

int arr[200000];
int cnt=0;


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int len;
    int temp;
    cin>>len;
    int number;
    for(int i=0;i<len;i++){
        cin>>number;
        if(number!=0){
            arr[++cnt]=number;
            int n1=cnt;
            int n2;
            
            while(n1>1){
                n2=n1;
                n1/=2;
                if(arr[n1]<arr[n2]){
                    
                    temp=arr[n1];
                    arr[n1]=arr[n2];
                    arr[n2]=temp;
                }   
                else{
                    break;
                }
            }
        }
        else{
             if(cnt==0){
                cout<<"0"<<"\n";
                cnt++;
            }
            else{
                cout<<arr[1]<<"\n";
                arr[1]=arr[cnt];
                int child=1;
                int parent=2;
                
                while(parent<cnt){
                    
                    if(arr[child]<arr[parent] or arr[child]<arr[parent+1]){
                        if(arr[parent]>arr[parent+1]){
                            temp=arr[parent];
                            arr[parent]=arr[child];
                            arr[child]=temp;
                            child=parent;
                            parent*=2;
                        }
                        else{
                            temp=arr[parent+1];
                            arr[parent+1]=arr[child];
                            arr[child]=temp;
                            child=parent+1;
                            parent=(parent+1)*2;
                        }
                    }
                    else
                        break; 
                }
                if((parent+1)==cnt){
                    if(arr[child]<arr[parent]){
                        temp=arr[parent];
                        arr[parent]=arr[child];
                        arr[child]=temp;                            
                    }
                }
                
            }
            cnt--;
        }    
    }
    return 0;
}