import pandas as pd

#df = pd.read_csv('pokemon_data.csv')
#print(df.head(3))

# df_xlsx = pd.read_excel('pokemon_data.xlsx')
# print(df_xlsx.head(5))

df = pd.read_csv('pokemon_data.txt' , delimiter='\t')
#print(df.head(5))
#df.head(5)



#       READ HEADERS
#print(df.columns)

#       READ EACH COLUMN
#print(df['Name'][0:5])   # or print(df.Name)
#print(df[['Name' , 'Type 1'  , 'HP']])

#       READ EACH ROW
#print(df.iloc[0:4])
# for index,row in df.iterrows():
#     print(index , row['Name'])
#print(df.loc[df['Type 1'] == "Grass"])


#       READ A SPECIFIC LOCATION(R,C)
#print(df.iloc[2,1])


#       Describe
#print(df.describe()) #view some basic statistical details like percentile, mean, std etc


#       SORT VALUES
#print(df.sort_values(["Type 1" , "HP"] ascending=False) #sort DataFrame by Name(A-Z) or opposite
#print(df.sort_values(['Type 1' , 'HP'], ascending = [1,0]))


#       MAKING CHANGES TO THE DATA
# df['Total'] = df["HP"] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
# df = df.drop(columns = ['Total']) #to remove a specific column

# df['Total'] = df.iloc[: ,4:10].sum(axis=1)
# cols = list(df.columns.values)
# df = df[cols[0:4] + [cols[-1]] + cols[4:12]]


#       SAVING OUR DATA
# df.to_csv('modified.csv' , index = False)  
#                                                ---> save the same file with new name
# df.to_excel('modified.xlsx', index= False)
# df.to_csv('modified.txt' , index= False , sep='\t' )


#       FILTERING DATA
# new_df = (df.loc[((df['Type 1']) == 'Grass') & (df['Type 2']=='Poison') & (df['HP']>70)])
# new_df.reset_index(drop=True , inplace=True)
# print(new_df)
# new_df.to_csv('filtered.csv' , index= True)

#df.loc[~df['Name'].str.contains('Mega')]    #"~" means that elements don't have to include 

#import re
#df.loc[df['Type 1'].str.contains('fire|grass' , flags=re. I, regex=True)]  #flags=re. --> means that capitalisation is not required 
#df.loc[df['Name'].str.contains('^pi[a-z]*' , flags=re. I, regex=True)]  #"^" means that the name should start from "pi" 


#       CONDITIONAL CHANGES
#df.loc[df['Type 1'] == 'Flamer' , 'Type 1']= 'Fire'  #--> change name Flamer into Fire
#df.loc[df['Type 1'] == 'Fire' , 'Legendary']= True  

#df = pd.read_csv('modified.csv')
# df['Total'] = df["HP"] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
# df.loc[df['Total']>500, ['Generation', 'Legendary']] ='TEST VALUE'


#       AGGREGATE STATISTICS (GROUPBY)
#df.groupby(['Type 1']).mean().sort_values('Attack' , ascending=False)    #groups by Attack of the 'Type' column
#df.groupby(['Type 1']).sum()

# df['count'] = 1
# print(df.groupby(['Type 1']).count()['count'])


#       WORKING WITH A LARGE AMOUNT OF DATA
# for df in pd.read_csv('modified.csv',chunksize=5):
#     print("CHUNK DF")
#     print(df)

# new_df = pd.DataFrame(columns=df.columns)
# for df in pd.read_csv('modified.csv', chunksize=5):
#     result = df.groupby(['Type 1']).coint()

#     new_df = pd.concat([new_df, result])
