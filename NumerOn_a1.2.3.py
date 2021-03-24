import random
import time
import math
import os

# グローバル変数
USER = 1
ANSWER = 2

### コマンドライン削除関数
def disp_clear() :
    if os.name == 'nt' :
        os.system('cls')
    else :
        os.system('clear')

### ファイルの新規作成確認
def check_file() :
    if os.path.exists('NumerOn_data.csv') :
        None
    else :
        f = open('NumerOn_data.csv',"a+")
        f.write('player,count\n')
        f.close()

### ファイル書き込み
def write_file(name1, count1, name2, count2) :
    f = open('NumerOn_data.csv','a')
    f.write('{0},{1},{2},{3}\n'.format(name1,count1,name2,count2))
    f.close()


### 3桁の数字が重複していないかどうかの判定(引数はint型の3つの整数，返り値はboolean)
def check_duplication(num1, num2, num3) :
    if num1 != num2 and num2 != num3 and num1 != num3:
        return True
    else : return False

### 引数としてintを受け取り，3つに分解する関数．返り値はint3つ
def numeric_decomposition(number) :
    num1 = int(number / 100)
    num2 = int((number % 100) / 10)
    num3 = int(number % 10)
    return num1, num2, num3

### キーボードからの入力を行う(引数なし，返り値はint型整数3つ)
def user_input(flag) :
    if flag == 1 :
        str1 = '数字を入力してください(半角数字) : '
        str2 = '数字は3桁の異なる整数です : '
    elif flag == 2 :
        str1 = '答えの数字を入力してください(半角数字) : '
        str2 = '答えの数字は3桁の異なる整数です : '
    else :exit()
    
    tmp_num = input(str1)
    while tmp_num.isdecimal() is False :
        tmp_num = input(str1)
    number = int(tmp_num)
    num = numeric_decomposition(number)
    # 4桁以上及び0以下の数字が入力された.もしくは同値があった場合の処理
    while number < 11 or number > 999 or check_duplication(num[0], num[1], num[2]) is False :
        tmp_num = input(str2)
        while tmp_num.isdecimal() is False :
            tmp_num = input(str2)
        number = int(tmp_num)
        num = numeric_decomposition(number)
    return num


### ユーザーの入力した数値を出力(引数はint型配列[要素数3つ]，返り値なし)
def print_number(input_num) :
    print(f'ユーザーの入力した数値 : {input_num[0]}{input_num[1]}{input_num[2]}')
    
### イート，バイトの判定(引数はint型配列[要素数3つ]を2つ，返り値はint型整数2つ)
def check_number(answer_num, input_num) :
    eat = 0; byte = 0

    for i in range (0, 3) :
        if input_num[i] == answer_num[i] :
            eat += 1
        elif input_num[i] in answer_num :
            byte += 1
        
    return eat, byte

### 
def run(answer_num) :
    # 予想回数を記録する変数
    count = 0

    while True :
        #予想回数を記録
        count += 1
        print(f'現在のターン数 : {count}')
        input_num = user_input(USER) #3桁のユーザーが入力した数字を1桁ずつ取得
        print_number(input_num)
        eat, byte = check_number(answer_num, input_num)
        print(f'eat: {eat}, byte: {byte}')
        if eat == 3 and byte == 0 :
            print('正解しました!')
            break
    
    return count

### 各プレイヤーのプレイ(引数はstr型の文字列とint型配列[要素数3つ]，返り値はint型整数1つ)
def play_game(name,answer_num) :
    print(f'{name}のプレイ')
    count = run(answer_num)
    time.sleep(2)
    disp_clear()

    return count

### プレイヤーの名前と数字を入力させる関数(引数は何番目のプレイヤーかを表すint1つ，返り値はstr及びint[3]の合計2つ)
def input_player_info(player) :
    name = input(f'プレイヤー{player}の名前を入力してください : ')
    num = user_input(ANSWER)
    return name, num

### 勝敗判定を行う関数(引数はそれぞれのプレイヤーのゲームクリアターン数を表すint2つとプレイヤーを表すstr2つ，返り値はなし)
def win_or_lose_dicision(count1, count2, player1, player2) :
    if count1 < count2 :
        print(f'勝者：{player1}')
    elif count1 > count2 :
        print(f'勝者；{player2}')
    else :
        print('引き分け')

def main() : 
    # nameはstr
    # answer_numはint型リスト(要素数3つ)

    # プレイヤー1が答えの3桁の数字を入力
    name1, answer_num1 = input_player_info(1)
    disp_clear()
    
    # プレイヤー2が答えの3桁の数字を入力
    name2, answer_num2 = input_player_info(2)
    disp_clear()

    # プレイヤー1のプレイ
    count1 = play_game(name1,answer_num2) # プレイヤー1がクリアするまでの予想回数を返り値で取得

    # プレイヤー2のプレイ
    count2 = play_game(name2,answer_num1) # プレイヤー2がクリアするまでの予想回数を返り値で取得
    
    win_or_lose_dicision(count1, count2, name1, name2) # 勝敗判定

    write_file(name1,count1,name2,count2)
    
    print('prog fin') # デバッグ

    time.sleep(2)
    disp_clear()


if __name__ == '__main__' :
    main()
