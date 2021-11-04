import math


reply = ['x','^']
replyto = ['*','**']
mathid = ['sin','cos','tan']

def get(text):
    for i in mathid:
        if(text.find(i)!=-1):
            fromnum = 0
            up = 0
            while(text.find("(",fromnum)!=-1):
                up+=1
                fromnum = text.find("(",fromnum)+1
            while(text.find(")",fromnum)!=-1):
                up-=1
                fromnum = text.find(")",fromnum)+1
                if up == 0:
                    end = fromnum-1
                    break
            pos = text[(text.find(i)):fromnum]
            gettext = get(pos[len(i)+1:end])
            text = text.replace(pos,gettext,1)

        gettext = str(eval(str(text[:text.find(")")])))
        print(text)
        count = eval(str(text))
        if(i == 'sin'):
            print(gettext)
            gettext = str(math.sin((math.pi/180)*float(count)))
            print(gettext)
        elif(i == 'cos'):
            gettext = str(math.cos((math.pi/180)*float(count)))
        elif(i == 'tan'):
            gettext = str(math.tan((math.pi/180)*float(count)))

        #number=eval(text[len(i)+1:])
        #print(number)
    
    return gettext

Text = "sin(90)="
for i in range(len(reply)):
    Text = Text.replace(reply[i],replyto[i])
print(get(Text))