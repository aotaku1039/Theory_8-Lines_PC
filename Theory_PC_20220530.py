import os
from unicodedata import numeric
os.system("cls") #コンソール画面消去

import time
import sys

g_setup_rate = [] #セットアップ率
g_pc_rate    = [] #パフェ率
g_setup_rate_total = 0 #セットアップ率合計


def inputRate():
    print("任意のルートの2巡目の進行率nを入力してください")
    print("Enter the progress rate n of the 2nd bag of any route.")
    print("")
    print("nの合計が5040以上になったら終わります")
    print("It will end when the total of n becomes 5040 or more.")
    
    tmp = inputAndCheck()
    global g_setup_rate_total
    
    if g_setup_rate_total + tmp > 5040:
        tmp = 5040 - g_setup_rate_total
        
    g_setup_rate.append(tmp)
    
    g_setup_rate_total += tmp
    print("")
    
    print("任意のルートの3巡目8段パフェ率nを入力してください")
    print("Enter the 3rd bag 8th stage pc rate n of any route.")
    g_pc_rate.append(inputAndCheck())
    print("")




def inputAndCheck():
    while True:
        input_text = input()
        flag = getFlag(input_text) #「.」の有無や純粋な数値であるかどうか
        
        if flag == 0: #「.」なし、純粋な数値
            input_num = int(input_text)
        
        elif flag == 1: #「.」あり、純粋な数値
            input_num = formatDecimalNumerator(input_text)
        
        else:
            continue #フラグが0でも1でもなければ純粋な数値ではないので弾く
        
        
        if 0 <= input_num <= 5040: #分子が0以上5040以下になる数値が打ち込まれていたときだけ通す
            return input_num


def getFlag(input_text):
    flag = -1
    
    if ("." in input_text) : #小数なら
        tmp_text = input_text.replace(".", "") #数値判別のために「.」を消す
        if tmp_text.isdecimal():
            return 1
        else:
            return -1
    else:
        if input_text.isdecimal(): #小数じゃないなら
            return 0
        else:
            return -1


def formatDecimalNumerator(text_decimal): #小数から分子に変換
    decimal = float(text_decimal)
    
    numerator = int(decimal * 50.4)
    if (decimal * 50.4 - numerator) > 0.5:
        numerator += 1
    
    return numerator




def printRate():
    print(f"進行率合計(Progress rate total)... {g_setup_rate_total} / 5040")
    print("")
    print("")



print("1巡目のセットアップ率nを入力してください")
print("Enter the setup rate n for the 1st bag.")
print("")
print("入力形式は、n / 5040のnの値 または「%」を省略した小数です(例...4936 97.94 など)")
print("The input format is the value of n in n / 5040 or a decimal fraction with \"%\" omitted (e.g. . .4936 97.94, etc.).")
print("")
print("小数入力の場合、n / 5040のnの値に自動で変換されます(例...99.09 → 4994)")
print("Decimal input is automatically converted to the value of n in n / 5040 (e.g. . .99.09 → 4994).")

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
