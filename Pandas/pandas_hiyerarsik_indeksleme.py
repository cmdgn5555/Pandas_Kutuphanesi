
import numpy as np
import pandas as pd
from pprint import pprint

veri = pd.Series(np.random.randn(15),
            index=[["a", "a", "b", "b", "b", "c", "c",
                    "d", "d", "d", "e", "e", "f", "f", "f"],
                   [10, 20, 10, 20, 30, 10, 20,
                    10, 20, 30, 10, 20, 10, 20, 30]])

print(veri)
print()
print(veri.index)
print()
print(veri["a"])
print()
print(veri["b"])
print()
print(veri["c"])
print()
print(veri["a": "d"])
print()
print(veri["c": "f"])
print()
print(veri.loc[["b", "d", "f"]])
print()
print(veri.loc[["a", "e"]])
print()
print(veri.loc[:, 10])
print()
print(veri.loc[:, 30])
print()
print(veri.unstack(level=1))
print()
print(veri.unstack(level=0))
print()
print(veri.unstack().stack())
print("_"*300)

df = pd.DataFrame(np.arange(12).reshape(4, 3),
                  index=[["a", "a", "b", "b"], [10, 20, 10, 20]],
                  columns=[["sayısal", "sayısal", "sözel"],
                           ["fizik", "kimya", "türkçe"]])

print(df)
print()
df.index.names = ["sınıf", "notlar"]
df.columns.names = ["alan", "dersler"]
print(df)
print()
print(df["sayısal"])
print()
print(df["sözel"])
print()
df = df.swaplevel(axis=1)
print(df)
print()
df = df.swaplevel("sınıf", "notlar")
print(df)
print()
print(df.sort_index(level=0, ascending=False))
print()
print(df.sort_index(level=1, ascending=False))
print()
print(df.sort_index(level=0, ascending=False, axis=1))
print()
print(df.sort_index(level=1, ascending=True, axis=1))
print()
print(df.sum(axis=0))
print()
print(df.sum(axis=1))
print("_"*300)

veri2 = pd.DataFrame({"x": range(50, 60),
                      "y": range(40, 30, -1),
                      "a": ["bir", "bir", "bir", "bir", "iki", "iki", "iki", "iki", "üç", "üç"],
                      "b": ["sarı", "beyaz", "mavi", "siyah", "kırmızı", "yeşil", "mor", "pembe", "eflatun", "turkuaz"]})

print(veri2)
print()
veri2.set_index(["x", "y"], inplace=True)
print(veri2)
print("_"*500)

veri3 = pd.DataFrame({"x": range(50, 60),
                      "y": range(40, 30, -1),
                      "a": ["bir", "bir", "bir", "bir", "iki", "iki", "iki", "iki", "üç", "üç"],
                      "b": ["sarı", "beyaz", "mavi", "siyah", "kırmızı", "yeşil", "mor", "pembe", "eflatun", "turkuaz"]})

print(veri3)
print()
veri3.set_index(["a", "b"], inplace=True, drop=False)
print(veri3)
print("_"*500)

veri4 = pd.DataFrame({"x": range(50, 60),
                      "y": range(40, 30, -1),
                      "a": ["bir", "bir", "bir", "bir", "iki", "iki", "iki", "iki", "üç", "üç"],
                      "b": ["sarı", "beyaz", "mavi", "siyah", "kırmızı", "yeşil", "mor", "pembe", "eflatun", "turkuaz"]})

print(veri4)
print()
veri4.set_index(["x", "y", "a"], inplace=True)
print(veri4)
print()
veri4.reset_index(level=0, inplace=True)
print(veri4)
print()
veri4.reset_index(level=1, inplace=True)
print(veri4)
print()
veri4.reset_index(inplace=True)
print(veri4)