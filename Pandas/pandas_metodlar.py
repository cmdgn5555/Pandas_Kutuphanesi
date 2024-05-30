
import pandas as pd
import numpy as np
from pprint import pprint

seri = pd.Series([10, 20, 30, 40, 50, 60],
                 index=["a", "b", "c", "d", "e", "f"])

print(seri)
print()
yeni_seri = seri.reindex(["d", "c", "f", "b", "e", "a"])
print(yeni_seri)

print("_"*200)

seri2 = pd.Series(data=["yeşil", "sarı", "pembe", "mor", "turuncu"],
                  index=[0, 2, 4, 6, 8])

print(seri2)
print()

yeni_seri2= seri2.reindex(range(10), method="bfill")
print(yeni_seri2)
print()

yeni_seri3 = seri2.reindex(range(10), method="ffill")
print(yeni_seri3)

print("_"*200)

seri3 = pd.Series(data=["ev", "araba", "uçak", "gemi"],
                  index=[0, 4, 9, 12])

print(seri3)
print()

yeni_seri4 = seri3.reindex(range(15), method="bfill")
print(yeni_seri4)
print()

yeni_seri5 = seri3.reindex(range(15), method="ffill")
print(yeni_seri5)

print("_"*500)

df = pd.DataFrame(np.arange(9).reshape(3, 3),
                  index=["a", "c", "d"],
                  columns=["serkan", "hasan", "taner"])

print(df)
print()

df2 = df.reindex(["c", "a", "d", "b"])
print(df2)
print()

df3 = df.reindex(columns=["hasan", "erdem", "taner"])
print(df3)
print()

print(df.loc[["d", "c", "a"]])


print("_"*500)

dizi1 = pd.Series(data=np.arange(8),
                  index=["a", "b", "c", "d", "e", "f", "g", "h"])

print(dizi1)
print()

yeni_dizi1 = dizi1.drop(["c", "d", "e"])
print(yeni_dizi1)
print()

yeni_dizi2 = dizi1.drop("a")
print(yeni_dizi2)

print("_"*500)

df4 = pd.DataFrame(data=(np.arange(36).reshape(6, 6)),
                   index=["mert", "ali", "eren", "can", "elif", "nur"],
                   columns=list("ABCDEF"))

print(df4)
print()
df4.drop(["mert", "ali"], inplace=True, axis=0)
print(df4)
print()
df4.drop("eren", inplace=True, axis=0)
print(df4)
print()
df4.drop(["A", "B", "C"], inplace=True, axis=1)
print(df4)
print()
df4.drop(["D", "E"], inplace=True, axis=1)
print(df4)

print("_"*500)

df5 = pd.DataFrame(data=(np.arange(36).reshape(6, 6)),
                   index=["mert", "ali", "eren", "can", "elif", "nur"],
                   columns=list("ABCDEF"))

print(df5)
print()
print(df5.mean(axis=1))
print()
print(df5.mean(axis=0))
print()
print(df5.sum(axis=1))
print()
print(df5.sum(axis=0))
print()
print(df5.median(axis=1))
print()
print(df5.median(axis=0))







