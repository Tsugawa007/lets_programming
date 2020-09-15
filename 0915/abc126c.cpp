#include<bits/stdc++.h>
using namespace std;
int main(void){
  int N,K;
  cin >> N >> K;
  int tmp = 1;
  int num_cnt = 0;
  while(K > tmp){
    tmp *= 2;
    num_cnt += 1;
  }
  double nums_list[N];
  for(int i = 1; i <= N; i++){
    for(int j = 0;j <= num_cnt;j++){
      if(i*pow(2,j) >= K){
        nums_list[i-1] = pow(0.5,j) *(1 / double(N));
        break;
      }
    }
  }
  double nums_sum = 0;
  for(int i= 0; i < N; i++){
    nums_sum += nums_list[i];
  }
  cout << setprecision(12) << nums_sum;
}
