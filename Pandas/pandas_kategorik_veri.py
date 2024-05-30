
import pandas as pd
import numpy as np

veri = pd.Series(["can", "ece", "can", "ali"] * 3)
print(veri)
print()
print(pd.unique(veri))
print()
print(pd.value_counts(veri))
print()

degerler = pd.Series([0, 1, 0, 2] * 5)
adlar = pd.Series(["ece", "can", "ali"])

print(adlar.take(degerler, axis=0))
print("_"*800)

print(veri)
print()

N = len(veri)
print(N)
print()

df = pd.DataFrame({"no": np.arange(N),
                   "isim": veri,
                   "notu": np.random.randint(50, 100, size=N),
                   "kilosu": np.random.uniform(60, 80, size=N)},
                  columns=["no", "isim", "notu", "kilosu"])

print(df)
print()
print(df["isim"])
print()
print(type(df["isim"]))
print("_"*50)

isim_kategori = df["isim"].astype("category")
print(isim_kategori)
print(type(isim_kategori))
print()

x = isim_kategori.values
print(x)
print()
print(x.categories)
print()
print(x.codes)
print()

df["isim"] = df["isim"].astype("category")
print(df["isim"])

örnek_kategori = pd.Categorical(list("xyzwq"))
print(örnek_kategori)
print()

meyveler_kategori = pd.Categorical(["çilek", "karpuz", "incir",
                                  "incir", "karpuz", "çilek", "çilek"])

print(meyveler_kategori)
print()

insanlar = ["cocuk", "bebek", "yaslı", "genc"]
kodlar = [0, 1, 2, 2, 0, 3, 3, 1, 1]

insanlar_kategori = pd.Categorical.from_codes(kodlar, insanlar, ordered=True)
print(insanlar_kategori)
print()
print(insanlar_kategori.as_ordered())