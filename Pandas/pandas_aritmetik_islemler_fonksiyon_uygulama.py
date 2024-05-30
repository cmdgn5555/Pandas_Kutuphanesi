
import pandas as pd
import numpy as np

seri1 = pd.Series(data=np.arange(6),
                  index=["a", "b", "c", "d", "e", "f"])

seri2 = pd.Series(data=np.arange(7),
                  index=["a", "b", "c", "d", "x", "y", "z"])

print(seri1)
print()
print(seri2)
print()
print(seri1 + seri2)

print("_"*200)

df1 = pd.DataFrame(data=np.arange(6).reshape(2, 3),
                   index=["murat", "anıl"],
                   columns=list("ABC"))

df2 = pd.DataFrame(data=np.arange(9).reshape(3, 3),
                   index=["murat", "anıl", "galip"],
                   columns=list("ACD"))

print(df1)
print()
print(df2)
print()
print(df1 + df2)
print()
print(df1.add(df2, fill_value=50))
print()
print(1 / df1)
print()
print(2 * df2)
print()
print(df1.mul(3))
print()
print(df1.sub(20))
print()
print(df2.div(5))
print()
print(df2.pow(4))
print()
print(df2.add(df1, fill_value=100))

print("_"*300)

df3 = pd.DataFrame(data=np.arange(9).reshape(3, 3),
                   index=["sercan", "erdem", "merve"],
                   columns=list("ACD"))

print(df3)
print()
s = df3.iloc[0]
print(s)
print()
print(df3 - s)
print()
s2 = df3["D"]
print(s2)
print()
print(df3.sub(s2, axis=0))
print()
s3 = df3["A"]
print(s3)
print()
print(df3.add(s3, axis=0))
print()
s4 = df3["C"]
print(s4)
print()
print(df3.mul(s4, axis=0))

print("_"*500)

veri = pd.DataFrame(np.random.randint(-5, 5, size=(4, 3)),
                    columns=list("ABC"),
                    index=["fatih", "emel", "deniz", "önder"])
print(veri)
print()
print(np.abs(veri))
print()
#print(np.transpose(veri))
#print()
print(np.product(veri))

print("_"*500)

veri2 = pd.DataFrame(np.random.randint(-10, 10, size=(4, 3)),
                    columns=list("ABC"),
                    index=["john", "jack", "tom", "dennis"])

print(veri2)
print()

fonk = lambda x: x.max() - x.min()
print(veri2.apply(fonk))
print()

fonk2 = lambda x: x.median() + x.median()
print(veri2.apply(fonk2))
print()

fonk3 = lambda x: x.min() / x.max()
print(veri2.apply(fonk3))
print()

fonk4 = lambda x: np.abs(x.max()) ** np.abs(x.min())
print(veri2.apply(fonk4))
print()

fonk5 = lambda x: x.min() * x.max()
print(veri2.apply(fonk5, axis=0))
print()
print(veri2.apply(fonk5, axis=1))
print()

fonk6 = lambda x: x.min() + x.max()
print(veri2.apply(fonk6, axis=0))
print()
print(veri2.apply(fonk6, axis=1))
print()

def üs_al(x):
    return x ** 2

print(veri2.apply(üs_al))
print()

def küp_al(x):
    return x ** 3

print(veri2.apply(küp_al, axis=1))

def ikiye_böl(x):
    return x / 2

print(veri2.apply(ikiye_böl, axis=1))









