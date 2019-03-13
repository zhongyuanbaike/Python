# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 00:45:20 2018

@author: 武状元
"""
import requests
import json

def get_TecentData(count=4,rank=0):
    url='https://xingyun.map.qq.com/api/getXingyunPoints'
    paload={'count':count,'rank':rank}
    dumpPaload = json.dumps(paload)
    response=requests.post(url,dumpPaload)
    print(f"dumpPaload = {dumpPaload}")
    #soup=BeautifulSoup(response.text,'lxml')
    #datas=soup.select('body')
    datas=response.text

    file_name='TecentData\data.txt'
    with open(file_name,'a') as f:
        for data in datas:
            #data=data.text
            f.write(data)
            

if __name__ =='__main__':
    #while(1):
        for i in range(4):
            get_TecentData(4,i)

