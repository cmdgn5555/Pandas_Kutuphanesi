
import pandas as pd
import numpy as np

vs = pd.DataFrame({"anahtar": list("ABC") * 2,
                   "veri1": range(6),
                   "veri2": np.arange(5, 11)})

print(vs)
print()

grup = vs.groupby(by="anahtar")

print(grup.aggregate([max, np.median, min]))
print()
print(grup.aggregate({"veri1": max, "veri2": max}))
print()
print(grup.aggregate({"veri1": min, "veri2": min}))
print("\n\n")

def fark(x):
    return x.max() - x.min()

print(grup.aggregate(fark))
print("_"*100)

def topla(x):
    return x.min() + x.max()

print(grup.aggregate(topla))
print("_"*100)

def bölüm(x):
    return x.max() / 2

print(grup.aggregate(bölüm))
print("_"*100)

def carpim(x):
    return x.min() * 2

print(grup.aggregate(carpim))

print("_"*750)

veri = pd.DataFrame({"harf": list("ABC") * 4,
                     "sayı": ["bir", "iki"] * 6,
                     "v1": np.random.randint(0, 50, size=(12,)),
                     "v2": np.arange(70, 93, 2)})

print(veri)
print("\n")

grupla = veri.groupby(["harf", "sayı"])
grupla_v1 = grupla["v1"]
print(grupla_v1.aggregate("mean"))
print("_"*50)

grupla = veri.groupby(["harf", "sayı"])
grupla_v2 = grupla["v2"]
print(grupla_v2.aggregate("max"))
print("_"*50)

grupla = veri.groupby(["harf", "sayı"])
grupla_v2 = grupla["v2"]
print(grupla_v2.aggregate("min"))
print("_"*50)

grupla = veri.groupby(["harf", "sayı"])
grupla_v1 = grupla["v1"]
print(grupla_v1.aggregate([fark, topla, "prod"]))
print("_"*50)

grupla = veri.groupby(["harf", "sayı"])
grupla_v2 = grupla["v2"]
print(grupla_v2.aggregate([("bölüm_sonuclar", bölüm), ("carpim_sonuclar", carpim)]))
print("_"*50)

grupla = veri.groupby(["harf", "sayı"])
fonk = ["mean", "count", "max"]
sonuc = grupla.aggregate(fonk)
print(sonuc)
print("_"*50)

grupla = veri.groupby(["harf", "sayı"])
fonk = ["min", "sum"]
sonuc2 = grupla.aggregate(fonk)
print(sonuc2)
print()
print(sonuc2["v2"])
print()
print(sonuc2["v1"])
print("_"*50)

grupla = veri.groupby(["harf", "sayı"])
sonuc3 = grupla.aggregate({"v1": ["max", "mean"], "v2": ["min", "sum"]})
print(sonuc3)
print("_"*50)

grupla1 = veri.groupby(["harf", "sayı"], as_index=False).sum()
print(grupla1)
print("_"*50)

grupla2 = veri.groupby(["harf", "sayı"], as_index=False).prod()
print(grupla2)
print("_"*50)

grupla3 = veri.groupby(["harf", "sayı"], as_index=False).min()
print(grupla3)
print("_"*2000)

print(veri)
print()

gr = veri.groupby("harf")
fonksiyon1 = gr["v2"].apply(lambda x: x.describe())
print(fonksiyon1)
print("_"*50)

gr = veri.groupby("harf")
fonksiyon2 = gr["v1"].apply(lambda x: x.sum())
print(fonksiyon2)
print("_"*50)

gr = veri.groupby("harf")
fonksiyon3 = gr["v1"].apply(lambda x: x.div(2))
print(fonksiyon3)
print("_"*750)

mat = pd.DataFrame({"sınıf": list("AB") * 3,
                    "ogrenciler": ["mehmet", "halim", "eda", "deniz", "ece", "can"],
                    "puan": [85, np.nan, 45, 60, np.nan, 100]})

print(mat)
print()
gr2 = mat.groupby("sınıf")
toplam = gr2.sum()
print(toplam)
print()

fonksiyon4 = lambda x: x.fillna(0)
a = gr2.apply(fonksiyon4)
print(a)

deger = {"A": 150, "B": 250}
fonksiyon5 = lambda x: x.fillna(deger[x.name])
b = gr2.apply(fonksiyon5)
print(b)

deger2 = {"A": 500, "B": 550}
fonksiyon6 = lambda x: x.fillna(deger2[x.name])
c = gr2.apply(fonksiyon6)
print(c)
print("_"*500)

dosya = pd.read_csv("vgsalesGlobale.csv")
print(dosya.head().to_string())

gr5 = dosya.groupby("Genre")
toplam5 = gr5.sum()
print(toplam5)
print()

fonksiyon7 = lambda x: x.fillna(0)
x = gr5.apply(fonksiyon7)
print(x.to_string())










