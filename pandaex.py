import pandas as pd
import numpy as np
df=pd.read_csv('intmark.csv')
print(df)
df[['int1','int2','int3','ass','seminar']]=df[['int1','int2','int3','ass','seminar']].fillna(0)
df.iloc[:, 2:5] = np.sort(df.iloc[:, 2:5], axis=1)[:,::-1]
print(df)
print(len(df))
internel=[]
def mark(m):
  sm=sum(m)
  internel.append(sm)
for i in range(len(df)):
  li=(df.iloc[i,[2,3,5,6]]).values.tolist()
  mark(li)
print(internel)

df['Total_Mark']=internel
print(df)
df.to_csv('intmark.csv',index=False)
