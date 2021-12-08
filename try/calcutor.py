import math
from os import replace, system

from mathonly.Trigonometric import *
from mathonly.sqrl import *


reply = [['*','x','×','ｘ','＊'],
['**','^','︿','＊＊'],
['+','＋'],
['-','－'],
['/','／'],
]

mathid = ['sin','cos','tan','csc','sec','cot','log']



def calcu(text):
    text = (text.replace('(','')).replace(')','')
    print(text)
    text = eval(text)
    return str(text)



def get(text):
    text = str(text)
    while(text.find(")")!=-1):
        count = text.find(")")
        while(text[count]!="("):
            count -=1
            if(count==-1):
                return "括弧放置錯誤"
        getto = text[count:text.find(")")+1]
        turnto = calcu(getto)
        for i in range(len(mathid)):
            if(text[count-3:].find(mathid[i])==0):
                if(i==0):
                    turnto = str(sin(float(turnto)))
                elif(i==1):
                    turnto = str(cos(float(turnto)))
                elif(i==2):
                    turnto = str(tan(float(turnto)))
                    if(turnto=="tan極端值(錯誤)"):
                        return "tan極端值(錯誤)"
                elif(i==3):
                    turnto = str(csc(float(turnto)))
                elif(i==4):
                    turnto = str(sec(float(turnto)))
                elif(i==5):
                    turnto = str(cot(float(turnto)))
                    if(turnto=="cot極端值(錯誤)"):
                        return "cot極端值(錯誤)"
                elif(i==6):
                    turnto = str(log(turnto))
                    if(turnto=="對數給予資料錯誤"):
                        return "對數給予資料錯誤"
                
                getto = mathid[i]+getto
        text = text.replace(getto,turnto)
    text = eval(text)
    
    return text


Text = "sin(sin(90)*30)="
Text = Text[:-1]
for i in range(len(reply)):
        for j in range(1,len(reply[i])):
            Text = Text.replace(reply[i][j],reply[i][0])
print(get(Text))