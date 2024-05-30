
import pandas as pd
import numpy as np

data = np.arange(0, 21)
print(data)
print("_"*30)

ceyrek = pd.qcut(data, 4)
print(ceyrek)
print("_"*30)
print(type(ceyrek))
print("_"*30)

ceyrek2 = pd.qcut(data, 4, labels=["q1", "q2", "q3", "q4"])
print(ceyrek2)
print("_"*30)

aralık = pd.Series(ceyrek, name="ceyrek")
print(aralık)
print("_"*30)

print(pd.Series(data))
print("_"*30)

print(pd.Series(data).groupby(aralık).aggregate(["count", "min", "max", "sum"]))
print("_"*500)


say = pd.Series(np.random.randn(1000))
print(say)
print()

etiket = pd.Series(["a", "b", "c", "d"] * 250)
print(etiket)
print()

kategori = etiket.astype("category")
print(kategori)
print()

print(etiket.memory_usage())
print()
print(kategori.memory_usage())
print("_"*500)

s = pd.Series(["ali", "can", "ali", "eda", "can", "eda"] * 2)
print(s)
print()

s_kategori = s.astype("category")
print(s_kategori)
print()

print(s_kategori.cat.codes)
print()
print(s_kategori.cat.categories)
print("_"*50)

yeni_kategori = ["ali", "can", "eda", "veli", "ece"]

print(s_kategori.cat.set_categories(yeni_kategori))
print("_"*50)

s2_kategori = s_kategori[s_kategori.isin(["ali", "can"])]
print(s2_kategori)
print()

print(s2_kategori.cat.remove_unused_categories())
print("_"*800)

print(s_kategori)
print("\n")
print(pd.get_dummies(s_kategori))








