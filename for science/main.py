from gif import *
import os

if __name__ == "__main__":
    start=1
    while(start==1):
        count = input("請輸入波數：")
        a=[]
        for i in range(int(count)):
            tmp =  input(f"請輸入第{i+1}個波的位置：").split(',')
            i={"x":tmp[0],"y":tmp[1]}
            a.append(i)
        os.system("cls")
        print("====================\n\n**正在處理資料**\n\n====================")
        getgif(a)
        test = input("輸入N離開，其他任意鍵繼續：")
        if test == "N" or test == "n":
            start=0