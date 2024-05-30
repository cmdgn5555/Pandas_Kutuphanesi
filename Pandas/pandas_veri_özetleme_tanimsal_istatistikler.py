
import pandas as pd
import numpy as np

df = pd.DataFrame(data=[[2, np.nan], [8, - 6],
                  [np.nan, np.nan], [4, -10]],
                  index=["a", "b", "c", "d"],
                  columns=["bir", "iki"])

print(df)
print()
print(df.sum())
print()
print(df.sum(axis=1))
print()
print(df.mean(axis=1))
print()
print(df.mean(axis=1, skipna=False))
print()
print(df.sum(axis=1, skipna=False))
print()
print(df.idxmax())
print()
print(df.idxmax(axis=1))
print()
print(df.idxmax(axis=1, skipna=False))
print()
print(df.idxmin())
print()
print(df.idxmin(axis=1))
print()
print(df.idxmin(axis=1, skipna=False))
print()
print(df.cumsum(axis=0))
print()
print(df.cumsum(axis=0, skipna=False))
print()
print(df.cumsum(axis=1))
print()
print(df.cumsum(axis=1, skipna=False))
print()
print(df.describe())
print("_"*100)

iris = pd.read_table("iris.txt")
print(iris.head())
print()
print(iris["Canak_yaprak_boyu"].corr(iris["Tac_yaprak_eni"]))
print()

s = pd.Series(["b", "b", "b", "k", "k", "k", "a", "a", "m", "m"])
print(s)
print(s.unique())
print()
print(s.value_counts())
print()
print(s.isin(["a", "c", "k", "p"]))
print()
print(s.isin(["b", "ü", "x"]))
print()
kontrol = s.isin(["a", "b"])
print(s[kontrol])


