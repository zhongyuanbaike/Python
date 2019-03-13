import pandas as pd
from datetime import datetime

reader = pd.read_csv('F:\\data\\All1-12.txt')

df=pd.DataFrame(reader)

df.columns = ['date', 'b', 'c', 'd']

df['date'] = pd.to_datetime(df['date']) #将数据类型转换为日期类型
df = df.set_index('date') # 将date设置为index

i=15
num_1=str(i)
num_2=str(i+1)
df = df['2016-01-'+num_1+' 21:00:00':'2016-01-'+num_2+' 00:00:00']

df.to_csv('F:\\timedata\\15.txt')




