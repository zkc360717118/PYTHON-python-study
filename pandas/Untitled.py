
# coding: utf-8

# In[2]:


import pandas as pd
# 读csv
df = pd.read_csv('pokemon_data.csv')
# print(df.head(3))
# print(df.tail(2))

# 读xlsx
# dc_xlsx = pd.read_excel('pokemon_data.xlsx')
# print(dc_xlsx.head(1))
# print(dc_xlsx.tail(1))

#读txt
# dc_txt = pd.read_csv('pokemon_data.txt',delimiter='\t')
# print(dc_txt.head(1))
# print(dc_txt.tail(1))


# In[26]:



#读取header
# print(df.columns)
#读每一列/多列
# print(df['Name'])
# print(df[['Name','HP']])  
# print(df.Name)  
# print(df['Name'][0:5])  #打印5行

#读每一行
# print(df.head(4)) # 前4行
# print(df.iloc[1]) #打印index是1的那一行数据。
# print(df.iloc[1:3]) #打印index是1到3的数据。

# for index,row in df.iterrows():
#     print(index,row['Name'])

df.loc[df['Type 1'] == "Fire"] # loc 传递的表达式有了过滤的效果

#读特定的某1个位置 location(r,c)
# print(df.iloc[2,1]) 


# In[37]:


# SORT  /  DESCRIBING DATA
# df.describe() #可以把数据集中的常用统计数据matrix 给到我们，比如最大，最小，数量，平均。。。。

# df.sort_values("Name") #使用name 排序
# df.sort_values('Name',ascending=False) #使用name 排序  这里name 用双引号会报错
# df.sort_values(['Name','HP'])
# df.sort_values(['Name','HP'],ascending=False)
df.sort_values(['Name','HP'],ascending=[1,0]) # 第一列升序，第二列降序
 


# In[6]:


# Change data

# df['Total'] = df['HP']+df['Attack']+df['Defense']+df['Sp. Atk']+df['Sp. Def']+df['Speed'] # 计算总数最垃圾的方式
# df = df.drop(columns= ['Total']) #可以去掉某一列
df['Total'] = df.iloc[:, 4:10].sum(axis=1) # better way

# 如何调整显示列的位置
cols = list(df.columns)
df = df[cols[0:4]+ [cols[-1]] + cols[4:12] ]

df.head(3)


# In[7]:


#SAVE DATA
df.to_csv('modified.csv') # index 也会写进文件
# df.to_csv('modified_without_index.csv',index=False) # index 不会写进文件
# df.to_excel('modified_without_index.xlsx',index=False) # index 不会写进文件
# df.to_csv('modified_without_index.txt',index=False,sep='\t') # index 不会写进文件 增加分隔符


# In[5]:


#FILTERING DATA
# df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP']>70) ]
new_df= df.loc[(df['Type 1'] == 'Grass') |   (df['Type 2'] == 'Poison') ]
# new_df = new_df.reset_index(drop=True) #重置原来的index，否则就是无序的。drop=False(默认会把旧的index作为 一个列保留，如不要就改成True)
# new_df.reset_index(drop=True,inplace=True) #重置原来的index，否则就是无序的。如果不想重新赋值，就使用inplace参数
# new_df

# df.loc[df['Name'].str.contains('Mega')]
# df.loc[~df['Name'].str.contains('Mega')] # ~ 取反。

import re
# df.loc[df['Type 1'].str.contains('Fire|Grass',regex=True)]
# df.loc[df['Type 1'].str.contains('Fire|Grass',flags=re.I,regex=True)] # 和上面有相同的结果，只是把忽略大小写单独用参数指定了
# df.loc[df['Name'].str.contains('^pi[a-z]*',flags=re.I,regex=True)] 

# df.loc[df['Type 1'] == 'Grass', 'Legendary'] = True  # 找到type 1 字段等于Grass的数据，然后把Legendary 对应的字段值改成Flamer
df.loc[df['Type 1'] == 'Grass', ['Generation','Legendary']] = ['test1','test2']
df


# In[17]:


# AGG STATISTICS
df = pd.read_csv('modified.csv')
# df.groupby(['Type 1']).mean() # 根据字段TYPE1 进行groupby 然后聚合方式是平均
# df.groupby(['Type 1']).mean().sort_values('Defense',ascending=False) #根据字段TYPE1 进行groupby 然后聚合方式是平均 ,最后按照Defense 排序
# df.groupby(['Type 1']).sum() # 根据字段TYPE1 进行groupby 然后聚合方式是求和
df['count']=1
# df.groupby(['Type 1']).count()['count'] # 根据字段Type 1 进行groupby 然后聚合方式是计数
df.groupby(['Type 1','Type 2']).count()['count'] # 根据字段Type 1 进行groupby 然后聚合方式是计数


# In[22]:


# Working with large amounts of data
for df in pd.read_csv('modified.csv',chunksize=5):
    print("CHUNK DF")
    print(df)


# In[24]:



new_df = pd.DataFrame(columns = df.columns)
for df in pd.read_csv('modified.csv',chunksize=5):
    results = df.groupby(['Type 1']).count()
    new_df = pd.concat([new_df,results])

new_df

