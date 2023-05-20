import pandas as pd
import numpy as np

# 
#
#There are two important datastructures in pandas, 1. DataFrame 2. Series.
print("-------------------Creating Frame and Series Objects---------------------------------------------")

#Series is a column like datastructure, can be created using a list.
series = pd.Series([1,2,3,4,5])
print("The defined series is ",series)
print("-------------------------------------------------------------------------------------------------")


#Dataframe is used to create a 2-dimensional datastructure.
adict ={"S.NO":[11,12,13,14],"cse-A":[1,2,3,4],"cse-B":[11,12,13,14]}
df = pd.DataFrame(adict)
print(df)

#There are few more ways to define a DataFrame
#1. Using List of List
#2. Using Numpy Arrays
#3. Using csv files.
#Lets explore each ones

#1.Using List of List
alist = [[1,'arun'],[2,'vijay'],[3,'vinay'],[4,'prabha']]

df = pd.DataFrame(alist,columns=['Roll.No','Name'])
print(df)



#2.Using Numpy Array
print("****Using Numpy Arrays****")
aray = np.array([1,2,3,4,5,6,7,8,9]).reshape(3,3).transpose()
df = pd.DataFrame(aray)
print(df)

#3.Define the dataframe from csv file datas.
#read_cse load the content from csv file and provides the reference to the  object 'data'
data = pd.read_csv('STUDENT.csv')

#displays the first five rows of data from the dataset.
print(data.head(5))
print("-------------------------------------------------------------------------------------------------")

#displays the last n rows of data from the dataset.
print(data.tail(5))

#Returns information about the Dataframes
info = data.info()
print(info)

#Returns the statistical description of a DataFrame
desc = data.describe()
print(desc)

print("------------------------------Data Selection------------------------------------------------------")
#selective data i.e., rows and columns from the DataFrame can be selected and used for further operations.

#Returns a the column 'IA1' aka the series from the dataframe 'data'
ia1_col = data['IA1']
print(ia1_col)

#Returns the details with IA1 greater than 50
ia1_above70 = data[data['IA1'] >=50]
print(ia1_above70)








