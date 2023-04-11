import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('titanic.csv')
print (df)
print(df.head())
print(df.shape)
print(df.describe())

#pandas series
col = df['Pclass']
#print(col)

col2 = df[['Pclass','Age','Fare']]
#print(col2)


df['Male'] = df['Sex'] == 'male'
#print(df)


#print(df['Age'].values)

#print(df[['Pclass','Age','Fare']]) #It will return table

#print(df[['Pclass','Age','Fare']].values) #It will return two dimensional array 

arr = df[['Pclass','Age','Fare']].values

#print(arr.shape)

#Array Indexing
#print(arr[0,1])  #First row Second column

#print(arr[2])   #Particular row ; I want third row.
#print(arr[:,2]) #Prticular column ; I want third column(age).

#Masking is a kind of comparision

mask = arr[:,1] < 18
#print(mask)
print(arr[mask])
print(mask.sum())

plt.scatter(df['Age'],df['Fare'])








