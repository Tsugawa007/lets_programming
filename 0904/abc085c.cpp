#include<bits/stdc++.h>
using namespace std;
int main(void){
  int N,S;
  cin >> N >> S;
  int x = -1, y = -1, z = -1;
  for(int i = 0; i < N+1;i++){
    for(int j = 0; j < N+1;j++){
      if(N-(i+j) >= 0 & S == ( 10000*i + 5000*j + 1000*(N-(i+j)) )){
        x = i;
        y = j;
        z = N - (i+j);
        break;
      }
    }
  }
  cout << x << " " << y << " " << z;
}
