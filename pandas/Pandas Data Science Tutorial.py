
# coding: utf-8

# ## Loading data into Pandas

# In[6]:


import pandas as pd

df = pd.read_csv('pokemon_data.csv')

# print(df.head(5))

# df_xlsx = pd.read_excel('pokemon_data.xlsx')
# print(df_xlsx.head(3))

# df = pd.read_csv('pokemon_data.txt', delimiter='\t')

# print(df.head(5))

df['HP']


# ## Reading Data in Pandas

# In[55]:


#### Read Headers
df.columns

## Read each Column
#print(df[['Name', 'Type 1', 'HP']])

## Read Each Row
#print(df.iloc[0:4])
# for index, row in df.iterrows():
#     print(index, row['Name'])
#df.loc[df['Type 1'] == "Grass"]

## Read a specific location (R,C)
#print(df.iloc[2,1])


# ## Sorting/Describing Data

# In[56]:


df.sort_values(['Type 1', 'HP'], ascending=[1,0])

df


# ## Making changes to the data

# In[57]:


#df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']

# df = df.drop(columns=['Total'])

df['Total'] = df.iloc[:, 4:10].sum(axis=1)

cols = list(df.columns)
df = df[cols[0:4] + [cols[-1]]+cols[4:12]]

df.head(5)


# In[58]:


45+49+49+65+65+45


# ## Saving our Data (Exporting into Desired Format)

# In[59]:


# df.to_csv('modified.csv', index=False)

#df.to_excel('modified.xlsx', index=False)

df.to_csv('modified.txt', index=False, sep='\t')



# ## Filtering Data

# In[66]:


new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]

new_df.reset_index(drop=True, inplace=True)

new_df

new_df.to_csv('filtered.csv')


# 
# ## Conditional Changes

# In[31]:




# df.loc[df['Total'] > 500, ['Generation','Legendary']] = ['Test 1', 'Test 2']

# df

df = pd.read_csv('modified.csv')

df


# ## Aggregate Statistics (Groupby)
# 

# In[105]:


df = pd.read_csv('modified.csv')

df['count'] = 1

df.groupby(['Type 1', 'Type 2']).count()['count']





# ## Working with large amounts of data
# 
# 

# In[115]:


new_df = pd.DataFrame(columns=df.columns)

for df in pd.read_csv('modified.csv', chunksize=5):
    results = df.groupby(['Type 1']).count()
    
    new_df = pd.concat([new_df, results])
    

    




# In[ ]:





