# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 20:01:57 2019

@author: 武状元
"""
import pandas as pd

df = pd.DataFrame(pd.read_csv('gdpoi.txt',header=0)) 
df['class']=None

#print(df.head())
for i in range(df.shape[0]):
    print(i)
    #df['type']=df['dtype'][i].split(';')[0]
    type=df['dtype'][i].split(';')[0]
    #type1=df['dtype'][i].split(';')[1]
    #type2=df['dtype'][i].split(';')[2]
    if ((type == "道路附属设施") | (type == "交通设施服务")):
        df['class'][i]='交通运输'
    elif  (type == "科教文化服务"):
        df['class'][i]='教育'
    elif  (type == "公司企业"):
        df['class'][i]='公司企业'
    elif  (type == "商务住宅"):
        df['class'][i]='住宅'
    elif  (type == "风景名胜"):
        df['class'][i]='绿地'
    elif  (type == "政府机构及社会团体"):
        df['class'][i]='政府机构'
    elif  ((type == "餐饮服务") | (type == "购物服务") | (type == "金融保险服务") | (type == "摩托车服务") | (type == "汽车服务") | (type == "汽车维修") | (type == "汽车销售") | (type == "生活服务") | (type == "住宿服务") | (type == "医疗保健服务")):
        df['class'][i]='商业'
    else:
        df['class'][i]='其他'

df.to_csv("gdpoi_cl.txt", index=False)
print(df.groupby('class').count())