#include<bits/stdc++.h>
using namespace std;
int main(){
  int K,S,c = 0;
  cin >> K >> S;
  for(int i = 0; i < K+1;i++){
      for(int j = 0; j < K+1;j++){
        if(S -(i+j) <= K &&  0 <= S -(i+j) ){c += 1;}
      }
  }
  cout << c;
}
