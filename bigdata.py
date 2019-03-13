import pandas as pd

reader = pd.read_csv('F:\\world.txt',iterator=True,error_bad_lines=False)

chunk = reader.get_chunk(50000000)

df=pd.DataFrame(chunk)

df.dropna()
df.columns = ['date', 'b', 'c', 'd']

df['date'] = pd.to_datetime(df['date']) #将数据类型转换为日期类型
df = df.set_index('date') # 将date设置为index

i=24
num_1=str(i)
num_2=str(i+1)
df = df['2016-01-'+num_1+' 21:00:00':'2016-01-'+num_2+' 00:00:00']
print(df)
df_1 = df[df.b >= 31.15]
df_2 = df_1[df_1.b <= 32.7]
df_3 = df_2[df_2.c >= 118.23]
df_4 = df_3[df_3.c <= 119.3]
# df_4.to_csv('F:\\timedata\\1.txt',index = False)
df_4 = df.groupby(['b', 'c']).sum()
df_4.to_csv('F:\\timedata\\1.txt',encoding = 'utf-8')




