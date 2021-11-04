msg = "who are you,i you him"
if(msg.find(',')>0):
    question = msg[:msg.find(',')]
    votename = msg[msg.find(',')+1:].split()
    voted = {}
    for i in votename:
        voted[i] = 0
    print(voted['i'])