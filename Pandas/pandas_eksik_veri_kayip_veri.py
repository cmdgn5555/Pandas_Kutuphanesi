import pandas as pd
import numpy as np
from numpy import nan as NA

s = pd.Series(["ahmet", np.nan, "ali", "fahri", "taner", "oğuz"])
print(s)
print()
print(s.isnull())
print()
print(s.notnull())
s[5] = None
print(s)
print(s.isnull())
print()
s.dropna(axis=0, inplace=True, ignore_index=True)
print(s)
print("_"*500)

df = pd.DataFrame(data=[[16, 26, 36], [44, NA, 55], [NA, NA, NA],
                        [NA, NA, NA], [27, 37, 47], [NA, 19, 29]])
print(df)
print()
print(df.dropna(how="any", axis=0))
print()
print(df.dropna(how="all", axis=0))
print("_"*500)

df2 = pd.DataFrame(data=[[16, NA, 36, 46, 56, NA], [44, NA, 55, 66, 76, NA],
                         [54, NA, NA, NA, 98, NA], [55, NA, 22, 32, 42, NA]])

print(df2)
print()
print(df2.dropna(axis=1, how="any"))
print()
print(df2.dropna(axis=1, how="all"))
print()
print(df2.dropna(axis=0, thresh=3))
print()
print(df2.dropna(axis=1, thresh=4))
print("_"*500)

df3 = pd.DataFrame(data=[[16, 101, 36, 46, 56, 10], [44, 103, 55, 66, 76, 30],
                         [54, 102, NA, NA, NA, NA], [NA, NA, 22, 32, 42, NA],
                         [NA, NA, 24, 25, 26, 20], [91, 104, NA, 92, NA, 94]])

print(df3)
print()
df3.fillna(0, inplace=True)
print(df3)
print("_"*500)

df4 = pd.DataFrame(data=[[16, 101, 36, 46], [44, 103, 55, 66],
                         [54, 102, NA, NA], [NA, NA, 22, 32],
                         [NA, NA, 24, 25], [91, 104, NA, 92]])

print(df4)
print()
df4.fillna({0: 250, 1: 630, 2: 340, 3: 520}, inplace=True)
print(df4)
print("_"*500)

df5 = pd.DataFrame(data=[[16, 101, 36, 46], [44, 103, 55, 66],
                         [54, 102, NA, NA], [NA, NA, 22, 32],
                         [5, NA, 24, 25], [91, 104, NA, 92]])

print(df5)
print()
#df5.fillna(method="ffill", inplace=True, axis=0)
#print(df5)
#print()
#df5.fillna(method="ffill", inplace=True, axis=1)
#print(df5)
print()

#df5.fillna(method="bfill", inplace=True, axis=0)
#print(df5)
#df5.fillna(method="bfill", inplace=True, axis=1)
#print(df5)
print("_"*500)

df5 = pd.DataFrame(data=[[16, 101, 36, NA], [44, 103, 55, NA],
                         [NA, 102, NA, NA], [NA, NA, NA, NA],
                         [NA, NA, NA, NA], [NA, NA, NA, 92]])

print(df5)
print()
df5.fillna(method="bfill", inplace=True, axis=0, limit=3)
print(df5)
print("_"*500)

veri = pd.Series([6, 10, NA, 12, NA, 30])
print(veri)
print()
#veri.fillna(veri.max(), inplace=True)
#print(veri)
print()
#veri.fillna(veri.min(), inplace=True)
#print(veri)
print()
#veri.fillna(veri.mean(), inplace=True)
#print(veri)
print("_"*500)

df6 = pd.DataFrame(data=[[10, 20, NA, 60], [NA, 5, 25, 30],
                         [40, NA, 50, 100], [50, 100, 150, NA]])

print(df6)
print()
#print(df6.fillna(df6.mean(), axis=0))
#print(df6.fillna(df6.max(), axis=0))
#print(df6.fillna(df6.min(), axis=0))




