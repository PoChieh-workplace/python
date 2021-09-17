import random
import json

with open('setting.json','r',encoding='utf8') as jfile:
    setting = json.load(jfile)

a = input('ip：')
ram = int(random.random()*1000000000)
try:
    while(setting[f'{ram}']):
        pass
except:
    setting[f'{ram}']=f"{a}"

with open('setting.json','w') as jfile:
    json.dump(setting,jfile)