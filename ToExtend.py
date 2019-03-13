import pandas as pd

chunks = pd.read_csv('F:\\world.txt',iterator=True,error_bad_lines=False,skiprows=2400000000)
chunk = chunks.get_chunk(100000000)
df= pd.DataFrame(chunk)
chunk.columns = ['a', 'b', 'c', 'd']
df_1 = df[df.b >= 31.15]
df_2 = df_1[df_1.b <= 32.7]
df_3 = df_2[df_2.c >= 118.23]
df_4 = df_3[df_3.c <= 119.3]
df_4.to_csv('F:\\data\\25.txt',encoding = 'utf-8', index = False)
