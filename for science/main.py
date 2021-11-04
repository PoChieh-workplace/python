from cmds.math import *
from cmds.information import *
from cmds.get import *
from cmds.function import *
from cmds.print import *


if __name__ == "__main__":
    count = input("請輸入波數：")
    distance = input("請輸入個波源距離：")
    a = {}
    for i in range(int(count)):
        a[i] =  input(f"請輸入第{i+1}個波的衰減率：")