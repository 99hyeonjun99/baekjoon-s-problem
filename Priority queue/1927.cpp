#include <iostream>
#include <queue>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int len;
    cin>>len;

    priority_queue<int, vector<int>, greater<int>> q;

    for(int i=0;i<len;i++){
        int number;
        cin>>number;

        if(number==0){
            if(q.empty()){
                cout<<0<<"\n";
            }
            else{
                cout<< q.top()<<"\n";
                q.pop();
            }
        }
        else{
            q.push(number);
        }

    }
}
