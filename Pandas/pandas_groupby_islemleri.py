
import pandas as pd
import numpy as np
from pprint import pprint
from matplotlib import pyplot as plt

vs = pd.DataFrame({"anahtar1": list("aabbab"),
                   "anahtar2": ["bir", "iki", "üç"] * 2,
                   "veri1": np.random.randint(10, 20, size=(6,)),
                   "veri2": np.random.randint(20, 30, size=(6,))})

print(vs)
print()
grup1 = vs["veri1"].groupby(by=vs["anahtar1"])
print(grup1.mean())
print()
grup2 = vs["veri2"].groupby(by=vs["anahtar2"])
print(grup2.mean())
print()
grup3 = vs["veri1"].groupby(by=vs["anahtar1"])
print(grup3.sum())
print()
grup4 = vs["veri2"].groupby(by=vs["anahtar2"])
print(grup4.sum())
print()
grup5 = vs["veri1"].groupby(by=[vs["anahtar1"], vs["anahtar2"]])
print(grup5.mean())
print()
grup6 = vs["veri2"].groupby(by=[vs["anahtar1"], vs["anahtar2"]])
print(grup6.sum())
print()
grup7 = vs["veri2"].groupby(by=[vs["anahtar1"], vs["anahtar2"]]).prod()
print(grup7)
print()
print(grup7.unstack())
print("_"*500)

vs1 = pd.DataFrame({"anahtar1": list("aabbab"),
                   "anahtar2": ["bir", "iki", "üç"] * 2,
                   "veri1": np.random.randint(10, 20, size=(6,)),
                   "veri2": np.random.randint(20, 30, size=(6,))})

print(vs1)
print()

g = vs1.groupby(["anahtar1", "anahtar2"]).mean()
print(g)
print()

g1 = vs1.groupby(["anahtar1", "anahtar2"]).sum()
print(g1)
print()

for name, group in vs1.groupby("anahtar1"):
    print(name)
    print(group)
print("_"*50)

for name, group in vs1.groupby("anahtar2"):
    print(name)
    print(group)
print("_"*50)

for name, group in vs1.groupby("veri1"):
    print(name)
    print(group)
print("_"*50)

for (x1, x2), group in vs1.groupby(["anahtar1", "anahtar2"]):
    print(x1, x2)
    print(group)

print("_"*100)

parca = dict(list(vs1.groupby("anahtar1")))
pprint(parca)
print()
print(parca["a"])
print()
print(parca["b"])

print("_"*100)

parca2 = dict(list(vs1.groupby("anahtar2")))
pprint(parca2)
print()
print(parca2["bir"])
print()
print(parca2["üç"])
print("_"*500)

oyun = pd.read_csv("vgsalesGlobale.csv")
print(oyun.head().to_string())
print()
print(oyun.dtypes)
print()
print(oyun.dropna().describe().to_string())
print()
print(oyun["Global_Sales"].mean())
print()
print(oyun["EU_Sales"].sum())
print()
print(oyun["Year"].median())
print("_"*100)

grupla = oyun.groupby("Genre")
print(grupla["Global_Sales"].count())
print("_"*200)
print(grupla["Global_Sales"].describe())
print("_"*200)
print(grupla.sum())
print("_"*200)
#görsel = grupla["Global_Sales"].sum()
#görsel.plot(kind="bar")
#plt.show()
print("_"*200)

print(oyun.head(20).to_string())
print("\n\n")

grupla2 = oyun.groupby("Publisher").head(20)
print(grupla2["Year"].sum())
print()
print(grupla2["Year"].describe())
print()
#görsel = grupla2["Year"].describe()
##görsel.plot(kind="bar")
#plt.show()
print("_"*1000)

grupla3 = oyun.groupby("Year")
print(grupla3["Other_Sales"].sum().describe())
#görsel = grupla3["Other_Sales"].sum().describe()
#görsel.plot(kind="bar")
#plt.show()
print("_"*1000)

meyve = pd.DataFrame(np.random.randint(10, 20, size=(4, 4)),
                     index=["nar", "muz", "kavun", "armut"],
                     columns=list("abcd"))

print(meyve)
print()

etiket = {"a": "mavi", "b": "yeşil", "c": "mavi", "d": "yeşil", "e": "pembe"}
print(etiket)
print()

gr = meyve.groupby(etiket, axis=1)
print(gr.sum())
print("_"*100)

s = pd.Series(etiket)
print(s)
print()

print(meyve.groupby(s, axis=1).count())
print("_"*100)

print(meyve.groupby(len).sum())
print("_"*500)

veri = pd.DataFrame(np.random.randint(20, 30, size=(4, 5)),
                    columns=[list("AAABB"), [1, 2, 3, 1, 2]])

print(veri)
print()
veri.columns.names = ["harf", "sayı"]
print(veri)
print()
toplam = veri.groupby(level="harf", axis=1).sum()
print(toplam)
print()

toplam2 = veri.groupby(level="sayı", axis=1).sum()
print(toplam2)
print("_"*500)

print(oyun.head().to_string())
print()
print(oyun.dtypes)
print()
print(oyun.dropna().describe().to_string())
print()
print(oyun["Global_Sales"].mean())
print()

gr1 = oyun.groupby("Genre")

print(gr1["Global_Sales"].count())
print()
print(gr1["Global_Sales"].describe())
print()
print(gr1.describe().mean())
print("_"*500)

grafik = gr1[["NA_Sales", "EU_Sales", "JP_Sales"]].sum()
print(grafik)
print()
ciz = grafik.plot(kind="bar")
plt.show()














