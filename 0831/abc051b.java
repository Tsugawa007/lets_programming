import java.util.*;
class Main{
  public static void main(String[]args){
    Scanner scan = new Scanner(System.in);
    int K = scan.nextInt();
    int S = scan.nextInt();
    int c = 0;
    
    for(int i = 0; i < K+1;i++){
      for(int j = 0; j < K+1;j++){
        if(S-(i+j) <= K && 0 <= S-(i+j)){ c+= 1;}
      }
    }
    System.out.println(c);
  }
}
