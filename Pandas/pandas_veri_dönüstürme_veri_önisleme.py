
import pandas as pd
import numpy as np

nt = [125, 480, 330, 275, 315, 250, 465, 150]

print(nt)
print("_"*50)
aralık = [100, 200, 300, 400, 500]
print(aralık)
print("_"*50)
puan = pd.cut(nt, aralık, right=False)
print(puan)
print("_"*50)
print(puan.codes)
print("_"*50)
print(puan.categories)
print("_"*50)
print(pd.value_counts(puan))
print("_"*50)
isim = ["düşük", "orta", "yüksek", "tavan"]
yeni_puan = pd.cut(nt, aralık, labels=isim)
print(yeni_puan)
print("_"*50)
puan2 = pd.cut(nt, 4)
print(puan2)
print("_"*500)

veri = np.arange(0, 100, 12)
print(veri)
print()
x = pd.qcut(veri, 4)
print(x)
print()
sayı = pd.value_counts(x)
print(sayı)
print("_"*500)

data = pd.DataFrame(np.random.randn(20, 4))
print(data)
print()
print(data.describe())
print()
sütun = data[2]
print(sütun)
print()
print(sütun[np.abs(sütun) > 1.5])
print()
print(np.sign(data).head())
print("_"*500)

data2 = pd.DataFrame(np.random.randn(10, 5))
print(data2)
print()
sütun2 = data2[4]
print(sütun2)
print()
print(sütun2[np.abs(sütun2) > 1])
print("_"*500)

veri2 = pd.DataFrame(np.arange(20).reshape(5, 4))
print(veri2)
print()
sira = np.random.permutation(5)
print(sira)
print()
print(veri2.take(sira, axis=0))
print()
print(veri2.sample(n=3))
print("_"*500)

veri3 = pd.DataFrame({"harf": ["b", "a", "c", "a", "b", "b"],
                      "sayı": range(6)})

print(veri3)
print()
print(pd.get_dummies(veri3["harf"]))
print()

veri4 = np.arange(10)
print(veri4)
print()
print(pd.get_dummies(pd.cut(veri4, 5)))
print("\n\n\n")

veri5 = np.arange(20)
print(veri5)
print()
print(pd.get_dummies(pd.cut(veri5, 6)).to_string())
print("\n\n\n")

veri6 = pd.DataFrame({"isim": ["ali", "can", "ege", "ege", "ali", "ege", "can", "ege", "can", "ege"],
                     "sayı": range(11, 21)})

print(veri6)
print()
print(pd.get_dummies(veri6["isim"]))



