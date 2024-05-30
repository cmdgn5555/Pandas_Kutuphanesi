
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

nt = pd.DataFrame({"sınıf": list("ABC") * 4,
                   "ders": ["mat", "fiz"] * 6,
                   "cinsiyet": list("EKEE") * 3,
                   "kardes": [1, 2, 5] * 4,
                   "puan": np.arange(40, 100, 5)})

print(nt)
print()
gr1 = nt.groupby("ders")["puan"].mean()
print(gr1)
print()
gr2 = nt.groupby("sınıf")["kardes"].sum()
print(gr2)
print()
gr3 = nt.groupby(["sınıf", "ders"])["puan"].aggregate("sum")
print(gr3)
print()
gr4 = nt.groupby(["ders", "sınıf"])["puan"].aggregate("mean").unstack()
print(gr4)
print("_"*100)

print(nt.pivot_table("kardes", index="ders", columns="sınıf"))
print()
print(nt.pivot_table(["kardes", "puan"],
                     index=["sınıf", "ders"],
                     columns="cinsiyet"))
print("\n")

print(nt.pivot_table(["kardes", "puan"],
                     index=["sınıf", "ders"],
                     columns="cinsiyet",
                     margins=True))

print("\n")

print(nt.pivot_table(["kardes", "puan"],
                     index=["sınıf", "ders"],
                     columns="cinsiyet",
                     margins=True,
                     fill_value=0))

print("\n")

print(nt)

print("\n")

kardes = pd.cut(nt["kardes"], [0, 2, 5])
print(nt.pivot_table("puan", ["ders", kardes], "sınıf", fill_value=0))
print()

print(nt.pivot_table(values="puan",
                     index="ders",
                     columns="sınıf",
                     aggfunc="prod",
                     margins=True,
                     margins_name="carpım"))

print("\n")

print(nt)
print()

print(nt.pivot_table(values="kardes",
                     index="ders",
                     columns="sınıf",
                     aggfunc="sum",
                     margins=True,
                     margins_name="toplam"))

print("\n")

print(nt)
print()

print(nt.pivot_table(values="puan",
                     index="ders",
                     columns="sınıf",
                     aggfunc="max",
                     margins=True,
                     margins_name="en büyük değer"))

print("\n")

print(nt)
print()

print(nt.pivot_table(values="puan",
                     index="ders",
                     columns="sınıf",
                     aggfunc="min",
                     margins=True,
                     margins_name="en küçük değer"))


print("\n")

print(nt)
print()

print(nt.pivot_table(index="ders",
                     columns="sınıf",
                     aggfunc={"kardes": "prod", "puan": "sum"}))

print("_"*500)

print(nt)
print()
print(pd.crosstab(index=nt["kardes"],
                  columns=nt["sınıf"]))

print("\n\n\n")

print(nt)
print()
print(pd.crosstab(index=[nt.kardes, nt.ders],
                  columns=nt.sınıf))

print("\n\n\n")

print(nt)
print()
print(pd.crosstab(index=nt.puan,
                  columns=[nt.sınıf, nt.ders]))
print("_"*200)

dogum = pd.read_csv("births.txt")
print(dogum.head())
print("\n")

dogum["onyıl"] = 10 * (dogum["year"] // 10)

print(dogum.pivot_table(values="births",
                        index="onyıl",
                        columns="gender",
                        aggfunc="sum"))

print()

sns.set()
dogum.pivot_table(values="births",
                  index="year",
                  columns="gender",
                  aggfunc="sum").plot()

plt.ylabel("yıllık toplam doğum")
plt.show()

print()

print(dogum.pivot_table(values="year",
                        index="day",
                        columns="month",
                        ).to_string())

#dogum.plot()
#plt.show()

print("\n\n\n")

#nt = pd.DataFrame({"sınıf": list("ABC") * 4,
#                   "ders": ["mat", "fiz"] * 6,
#                   "cinsiyet": list("EKEE") * 3,
#                   "kardes": [1, 2, 5] * 4,
#                   "puan": np.arange(40, 100, 5)})
#
#print(nt)
#print()
#
#print(nt.pivot_table(values="puan",
#                     index="sınıf",
#                     columns="ders"))
#sns.set()
#nt.plot(y="puan", kind="barh")
#plt.show()






