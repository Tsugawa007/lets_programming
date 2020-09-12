#include<stdio.h>
typedef struct{
  int y;
  int m;
  int d;
}Date;
void printDate(Date d){
  printf("%4d年%02d月%02d日",d.y,d.m,d.d);
}
int main(void){
  Date day;
  puts("日付を入力してください");
  printf("年:"); scanf("%d",&day.y);
  printf("月:"); scanf("%d",&day.m);
  printf("日:"); scanf("%d",&day.d);
  printDate(day);
}
