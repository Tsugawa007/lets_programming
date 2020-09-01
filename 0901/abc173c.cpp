#include<bits/stdc++.h>
using namespace std;
int main(){
  int H,W,K,ans = 0;
  cin >> H >> W >> K;
  string nums[H];
  for(int i = 0; i < H; i++){
    cin >> nums[i];
  }
  
  for(int i = 0; i < pow(2,H);i++){
    for(int j = 0; j < pow(2,W);j++){
      int c = 0;
      for(int x = 0; x < H; x++){
        for(int y = 0; y < W; y++){
          if( ((i>>x)&1) == 0 && ((j>>y)&1) == 0){
            if(nums[x][y] == '#'){c+=1;}
          }
        }
      }
      if(c == K){ans+= 1;}
    }
  }
  cout << ans;
  
}
