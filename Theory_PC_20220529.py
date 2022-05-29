import os
os.system("cls") #コンソール画面消去

import time
import sys

g_setup_rate = [] #セットアップ率
g_pc_rate    = [] #パフェ率
g_setup_rate_total = 0 #セットアップ率合計


def inputRate():
    print("任意のルートの2巡目の進行率nを入力してください(n / 5040) nの合計が5040以上になったら終わります")
    print("Enter the progress rate n of the 2nd bag of any route (n / 5040). It will end when the total of n becomes 5040 or more.")
    
    tmp = inputAndCheck()
    global g_setup_rate_total
    
    if g_setup_rate_total + tmp > 5040:
        tmp = 5040 - g_setup_rate_total
        
    g_setup_rate.append(tmp)
    
    g_setup_rate_total += tmp
    print("")
    
    print("任意のルートの3巡目8段パフェ率nを入力してください(n / 5040)")
    print("Enter the 3rd bag 8th stage pc rate n of any route (n / 5040). ")
    g_pc_rate.append(inputAndCheck())
    print("")



def inputAndCheck(): #入力とそのチェック
    while True:
        input_text = input()
        if input_text.isdecimal():
            input_num = int(input_text)
            if 0 <= input_num <= 5040: #0以上5040以下の数値が打ち込まれていたときだけ通す
                return input_num



def printRate():
    print(f"進行率合計(Progress rate total)... {g_setup_rate_total} / 5040")
    print("")
    print("")

print("1巡目のセットアップ率nを入力してください(n / 5040)")
print("Enter the setup rate n for the 1st bag (n / 5040). ")
g_1st_setup = inputAndCheck()
print("")
print("")


while(True):
    inputRate()
    printRate()
    
    if g_setup_rate_total >= 5040:
        break
    


def calc_rate():
    indexcnt = len(g_setup_rate)
    rate = 0
    
    for i in range(indexcnt):
        rate += g_setup_rate[i] * g_pc_rate[i]
    
    return rate



rate = calc_rate()

os.system("cls") #コンソール画面消去

printRate()
print("結果確率 小数第3位四捨五入で小数第2位まで(Result probability, rounded to two decimal places)")
print()
print(f"{rate} / {5040 ** 2}")
print(f"1巡目加味しない(1st bag irrelevant)...{rate / (5040 ** 2) * 100:.2f}% ({rate / (5040 ** 2) * 100}...%)")
print("")
print(f"{g_1st_setup * rate} / {5040 ** 3}")
print(f"1巡目加味(1st bag relevant.)...{g_1st_setup * rate / (5040 ** 3) * 100:.2f}% ({g_1st_setup * rate / (5040 ** 3) * 100}...%)")
print("")

tmp = input("Enterキー入力で終わります(Press Enter.)")
sys.exit()
