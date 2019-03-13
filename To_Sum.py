import pandas as pd

reader = pd.read_csv('F:\\to xinyijie\\shanghai.txt')

df=pd.DataFrame(reader)

df.dropna()
df.columns = ['b', 'c', 'd']
#df.drop(['a'], axis=1)

df_1 = df.groupby(['b', 'c']).sum()
df_1.to_csv('F:\\to xinyijie\\shanghai_sum.txt',encoding = 'utf-8',index=True)




