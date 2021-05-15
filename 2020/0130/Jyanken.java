import java.util.*;
import java.io.*;
public class Jyanken {



    public static int[] makeJyanken(int personNum, int choiceJyanken,int jyankenCnt){
        //コンピュータの手をランダムにするための変数
        long seed = 1000;
        Random rndSeed = new Random(seed);
        Random rndSeed2 = new Random();

        //２次元配列　randomChoiceの行の長さ：3  列:2
        int randomChoice[][]  = new int[3][2];
        randomChoice[0][0] = 0;
        randomChoice[0][1] = 1;

        randomChoice[1][0] = 0;
        randomChoice[1][1] = 2;

        randomChoice[2][0] = 1;
        randomChoice[2][1] = 2;

        //upperRandom  は0~2をランダムで出す(1~３行目をランダムで選ぶ)
        int upperRandom = rndSeed2.nextInt(3);

        //HashMap(Pythonで言う 辞書) [数値(グー、チョキ、パー)、その手を選んだCPの数]
        //あとで人数を追加していく

        /*　choiceListの例  CPの数　６人
        　　0(グー),２(2人のCPがグーを選んだ)
           1(チョキ),3(3人のCPがチョキを選んだ)       
        　　2(パー),１(1人のCPがパーを選んだ)        
        */

        Map<Integer,Integer> choiceList = new HashMap<Integer,Integer>();
        choiceList.put(0, 0);
        choiceList.put(1, 0);
        choiceList.put(2, 0);
        
    
        //HashMap　[数値(グー、チョキ、パー)、文字(グー、チョキー、パー)]　
        //ディスプレイ用
        Map<Integer,String> patternJyanken = new HashMap<Integer,String>();
        patternJyanken.put(0, "グー");
        patternJyanken.put(1, "チョキ");
        patternJyanken.put(2, "パー");

        //自分のジャンケンの手を出力する
        System.out.println("あなた:" + patternJyanken.get(choiceJyanken));

        //CPのジャンケンの手をランダムで選び、出力する
        for(int i = 0; i < personNum; i++){

            int tmpCp;

            //変数 jyankenCntが2の倍数でない(50%の確率)とき、課題2の仕様にする
            if(jyankenCnt % 2 == 1 ){
                tmpCp = randomChoice[upperRandom][rndSeed.nextInt(2)];
            }else{
                tmpCp = rndSeed.nextInt(3);
            }

            //CPが選んだ手をchoiceListに入れている
            choiceList.put(tmpCp, choiceList.get(tmpCp)+1);

            //CPが選んだ手を出力する
            System.out.println("CP:" + (i+1)  +patternJyanken.get(tmpCp));
        }

        //勝ち負けの判定をする関数　judgeJyankenに送っている
        //judeJyanken関数  (中身: [choiceList,自分がどの手を選んだか、CPの数])
        int[] ans = judgeJyanken(choiceList,choiceJyanken,personNum);

        return ans;
    }

    //配列ans (中身:　　勝ち負け[0...勝ち,1...負け,2...引き分け]　、残ったCPの数)

    //勝ち負けの処理を書くと、同じ処理のところがあるので、まとめました
    //judgeJyanken関数の中で使用する
    public static int[] jyankenA(Map<Integer, Integer> choiceList,int personNum){
        int ans[] = new int[2];
        ans[0] = 0;
        ans[1] = 0;
        return ans;
    }

    public static int[] jyankenB(Map<Integer, Integer> choiceList,int personNum){
        int ans[] = new int[2];
        ans[0] = 1;
        ans[1] = 0;
        return ans;
    }

    public static int[] jyankenC(Map<Integer, Integer> choiceList,int personNum){
        int ans[] = new int[2];
        ans[0] = 2;
        ans[1] = personNum;
        return ans;
    }

    //勝ち負け処理
    public static int[] judgeJyanken(Map<Integer, Integer> choiceList, int choiceJyanken,int personNum){
        int ans[] = new int[2];
        
        if(choiceList.get(0) == 0){
            if(choiceList.get(1) == 0){
                //a
                if(choiceJyanken == 0){
                    ans = jyankenB(choiceList,personNum); 
                }else if(choiceJyanken == 1){
                    ans = jyankenA(choiceList,personNum); 
                    
                }else{
                    ans = jyankenC(choiceList,personNum); 
                }
            }else if(choiceList.get(2) == 0){
                //b
                if(choiceJyanken == 0){
                    ans = jyankenA(choiceList,personNum); 
                }else if(choiceJyanken == 1){
                    ans = jyankenC(choiceList,personNum); 
                }else{
                    ans = jyankenB(choiceList,personNum); 
                }
            }else{
                //c
                if(choiceJyanken == 0){
                    ans = jyankenC(choiceList,personNum); 

                }else if(choiceJyanken == 1){
                    ans[0] = 0;
                    ans[1] = choiceList.get(1);
                }else{
                    ans = jyankenB(choiceList,personNum); 
                }

            }

        }else if(choiceList.get(1) == 0){

            if(choiceList.get(0) == 0){
                //d
                if(choiceJyanken == 0){
                    ans = jyankenA(choiceList,personNum); 
                }else if(choiceJyanken == 1){
                    ans = jyankenB(choiceList,personNum); 
                }else{
                    ans = jyankenC(choiceList,personNum);
                }
            }else if(choiceList.get(2) == 0){
                //e
                if(choiceJyanken == 0){
                    ans = jyankenC(choiceList,personNum); 
                }else if(choiceJyanken == 1){
                    ans = jyankenB(choiceList,personNum); 
                }else{
                    ans = jyankenA(choiceList,personNum); 
                }              
            }else{
                //f
                if(choiceJyanken == 0){
                    ans = jyankenB(choiceList,personNum); 
                }else if(choiceJyanken == 1){
                    ans = jyankenC(choiceList,personNum); 
                }else{
                    ans[0] = 0;
                    ans[1] = choiceList.get(2);
                }  

            }

        }else if(choiceList.get(2) == 0){
            if(choiceList.get(0) == 0){
                //g
                if(choiceJyanken == 0){
                    ans = jyankenA(choiceList,personNum); 
                }else if(choiceJyanken == 1){
                    ans = jyankenC(choiceList,personNum); 
                }else{
                    ans = jyankenB(choiceList,personNum); 
                }  
            }else if(choiceList.get(1) == 0){
                //h
                if(choiceJyanken == 0){
                    ans = jyankenC(choiceList,personNum); 
                }else if(choiceJyanken == 1){
                    ans = jyankenB(choiceList,personNum); 
                }else{
                    ans = jyankenA(choiceList,personNum); 
                } 
            }else{
                //i
                if(choiceJyanken == 0){
                    ans[0] = 0;
                    ans[1] = choiceList.get(0);
                }else if(choiceJyanken == 1){
                    ans = jyankenB(choiceList,personNum); 
                }else{
                    ans = jyankenC(choiceList,personNum); 
                } 

            }
        }else{
            ans = jyankenC(choiceList,personNum); 
        }
        return ans;

    }

    
}
