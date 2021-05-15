#include<bits/stdc++.h>
using namespace std;
int main(void){
  int N;
  cin >> N;
  float nums[N][2],max_distance;
  for(int i = 0; i< N; i++){
    cin >> nums[i][0] >> nums[i][1];
  }
  
  for(int j = 0; j < N; j++){
    for(int k = j+1; k < N;k++){
      if(max_distance < sqrt( pow((nums[k][0] - nums[j][0]),2)+ pow((nums[k][1] - nums[j][1]),2) )){
         max_distance = sqrt( pow((nums[k][0] - nums[j][0]),2)+ pow((nums[k][1] - nums[j][1]),2) );
      }
    }
  }
  cout << setprecision(10) <<  max_distance;
}
