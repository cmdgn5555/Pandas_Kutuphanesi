
import pandas as pd
import numpy as np

veri = pd.DataFrame(data=np.arange(100, 116).reshape(4, 4),
                    index=[list("aabb"), [1, 2] * 2],
                    columns=[["say", "say", "söz", "söz"],
                             ["mat", "ing"] * 2])

print(veri)
print()

veri.index.names = ["sınıf", "sınav"]
veri.columns.names = ["alan", "ders"]
print(veri)
print()

uzun = veri.stack(level=1)
print(uzun)
print()

uzun = veri.stack(level=0)
print(uzun)
print()

uzun = uzun.unstack(level=1)
print(uzun)
print()

uzun = uzun.unstack()
print(uzun)
print()

uzun = uzun.stack(level="alan")
print(uzun)
print()

uzun = uzun.stack(level="sınav")
print(uzun)
print()


uzun = uzun.stack(level="ders")
print(uzun)
print()

uzun = uzun.unstack("ders")
print(uzun)
print()

uzun = uzun.unstack("sınav")
print(uzun)
print()

uzun = uzun.unstack("alan")
print(uzun)
print()

uzun = uzun.unstack("sınıf")
print(uzun)

print("_"*500)

s1 = pd.Series(data=np.arange(10, 14), index=list("abcd"))
print(s1)
print()

s2 = pd.Series(data=np.arange(20, 23), index=list("cde"))
print(s2)
print()

birlestir = pd.concat([s1, s2], keys=["bir", "iki"])
print(birlestir)
print()

birlestir = birlestir.unstack()
print(birlestir)
print()

birlestir = birlestir.stack(dropna=False)
print(birlestir)
print()
print("_"*500)

stok = pd.DataFrame({"sebze": ["turp", "limon", "havuç"] * 2,
                     "renk": ["mor", "pembe"] * 3,
                     "adet": [3, 4, 5, 6, 1, 2]})

print(stok)
print()

print(stok.pivot(index="sebze", columns="renk", values="adet"))
print()

stok["degerler"] = np.random.randn(6)
print(stok)
print()

piv = stok.pivot(index="sebze", columns="renk")
print(piv)
print()

print(piv["degerler"])
print()
print(piv["adet"])
print("_"*500)

veri2 = pd.DataFrame({"ders": ["mat", "fiz", "edb"],
                      "ali": [60, 80, 95],
                      "ahmet": [40, 95, 100],
                      "mehmet": [95, 60, 35]})

print(veri2)
print()

grup = pd.melt(veri2, ["ders"], ignore_index=True)
print(grup)
print()

piv2 = grup.pivot(index="ders", columns="variable", values="value")
print(piv2)
print()

piv2 = piv2.reset_index()
print(piv2)













