#include<iostream>
#include <array>
using namespace std;
int main(){
    int N;
    cin >> N;
    std::array<int,1000> a;
    std::array<int,1000> ans_list;
    ans_list.fill(0);
    for(int i = 1; i < N+1;i++){
        cin >> a[i];
    }
    for(int i = 1; i < N+1;i++){
        int num_max = 0;
        if(ans_list[i-1] < ans_list[i-1]+a[i]){ans_list[i] = ans_list[i-1]+a[i];}
        if(ans_list[i-1]+a[i] < ans_list[i-1]){ans_list[i] = ans_list[i-1];}
    }
    int ans = 0;
    for(int j = 0; j <= N; j++){

        if(ans < ans_list[j]){ans = ans_list[j];}
    }
    cout << ans << endl;
}
