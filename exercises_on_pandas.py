#       create and display a one-dimensional array-like object containing an array of data
# import pandas as pd

# one_dim_arr = pd.Series([1,2,3,4,5,6,7,8])  #--> first column of indexes and second takes the data from input
# print(one_dim_arr)


#       create and display a DataFrame from a specified dictionary data which has the index labels
# import pandas as pd
# import numpy as np

# example_data = {'name':['Kristi', 'Andrew' , 'Mike' , 'Lana'],
#         'score':[10, 4, 5.5 , np.nan],
#         'attemps':[2, 4, 1, 0],
#         'qualify':['yes', 'yes' ,'no' , 'yes']}

# labels = ['a1', 'a2', 'a3', 'a4']
# df = pd.DataFrame(example_data, index = labels)
# print(df)


#       create a multi Index frame using two columns and using an Index and a column
# import pandas as pd

# df = pd.DataFrame({'school_code': ['s001', 's002', 's003', 's001', 's002', 's004'],
#     'class':['A', 'A', 'B', 'B', 'C', 'D'],
#     'name':['Will Smith' , 'Dwayne Johnson' , 'Brad Pitt' , 'Tom Kruise' , 'Dwayne Johnson' , 'Tom Holland'],
#     'weight':[65, 86 , 57 , 70 , 77 , 86],
#     'address':['street1' , 'street2' , 'street3' , 'street1', 'street2' , 'street4'],
#     't_id': ['t1' , 't2' , 't3' , 't4' , 't5' , 't6']})

# print("original DataFrame")
# print(df)
# print("MultiIndex using columns 't_id' and 'school_code': ")

# df1 = df.set_index(['t_id', 'school_code'])
# print(df1)
# print("\n MultiIndex using an Index and a column: ")
# df2 = df.set_index([pd.Index([0,1,2,3,4,5]), 't_id'])
# print(df2)


#       add leading zeros to the integer column
# import pandas as pd

# nums = {'amount': [10, 20, 40, 550, 989, 1, 971 , 34]}
# print("Original DataFrame")
# df = pd.DataFrame(nums)
# print(df)
# print("\n Add leading zeros")
# df['amount'] = df['amount'].apply(lambda x:'{0:0>4}'.format(x))
# print(df)


#       append rows to an existing DataFrame and display the combined data
# import pandas as pd

# df = pd.DataFrame({'student_id':['S1', 'S2' , 'S3' , 'S4', 'S5'],
#         'name':['Danniella Fenton' , 'Ryder Storey' , 'Bryce Jensen' , 'Ed Bernal' , 'Kwame Morin'],
#         'marks':[200, 210, 190 , 222 , 199]})
# s6 = pd.Series(['S6' , 'Scarlette Fisher' , 205], index = ['student_id' , 'name' , 'marks'])
# append = df.append(s6 , ignore_index=True)
# print("Original DataFrames: ")
# print(df)
# print("\nNew Row(s) ")
# print(s6)
# print("\nCombined Data: ")
# print(append)