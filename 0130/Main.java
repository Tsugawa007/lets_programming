import java.util.*;
import java.io.*;


public class Main{
    public static void main(String[]args) throws Exception{
    
        BufferedReader buf = new BufferedReader(new InputStreamReader(System.in));

        System.out.println("対戦人数を入力してください(1~10)");

        //対戦人数入力
        String mainLine = buf.readLine();
        int personNum = Integer.parseInt(mainLine);

        //対戦人数が1~10人の間ではないとき、終了する
        if(personNum  > 10 || personNum  < 1 ){
            System.out.println("正しい人数を入力してください");
            System.exit(1);
        }

        //課題２用 numJudgeがtrueだと、課題2の仕様にいく
        boolean numJudge = false;
        if(personNum  >= 3){
            numJudge = true;
        }

        //課題2の条件で使用する
        int jyankenCnt = 0;

        boolean flag = true;

        while(flag){
            System.out.println("じゃんけんぽん(0:グー・1:チョキ・2:パー)");
            String subLine = buf.readLine();
            int choiceJyanken = Integer.parseInt(subLine);
            switch(choiceJyanken){
                case 0:
                case 1:
                case 2:
                    if(numJudge == true){
                        //ジャンケンの回数
                        jyankenCnt++;
                    }
                    //JyankenクラスのmakeJyanken関数の帰り値を配列ansに送る
                    //makeJyanken関数　(中身: ジャンケンする人数、どの手を選んだか[0:グー・1:チョキ・2:パー]、ジャンケンの回数)
                    //配列ans (中身:　　勝ち負け[0...勝ち,1...負け,2...引き分け]　、残ったCPの数)
                    int[] ans = Jyanken.makeJyanken(personNum ,choiceJyanken,jyankenCnt);
                    if(ans[0] == 0){
                        if(ans[1] == 0){
                            System.out.println("あなたが勝ち残りました！　おめでとう！");
                            flag = false;
                        }else{
                            System.out.println("あなたの勝ちです。残りCP数:" + ans[1]);
                            personNum  = ans[1];
                        }
                    }else if(ans[0] == 1){
                        System.out.println("あなたの負けです。");
                        flag = false;
                    }else{
                        System.out.println("引き分けです。");
                    }
                    break;
                default:
                    System.out.println("正しい手を入力してください");
                    break;
            }      

            
        
        }
        

    }



}