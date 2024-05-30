
import pandas as pd
import numpy as np
import sys

df1 = pd.read_table("veri2.txt", sep=",",
                    header=None,
                    names=["isim", "puan", "cinsiyet"],
                    index_col="isim")
print(df1)
print("_"*500)

df2 = pd.read_table("veri3.txt", sep=",",
                    index_col=["ders", "isim"])
print(df2)
print("_"*500)

df3 = pd.read_table("veri4.txt", sep=",",
                    skiprows=[0, 1, 2],
                    usecols=[1, 2])
print(df3)
print("_"*500)

eksik_veriye_cevir = {"puan": [-5], "cinsiyet": [-33, "Efe"]}

df4 = pd.read_table("veri5.txt",
                    sep=",",
                    na_values=eksik_veriye_cevir)
print(df4)
print()
print(df4.isnull())
print()
print(df4.notnull())
print("_"*500)

df5 = pd.read_table("veri.txt")
print(df5)
df5.to_csv("yeni_veri2.csv", sep="|")
print()
df5.to_csv(sys.stdout, sep="|")
print()
df6 = pd.read_table("veri2.txt")
print(df6)
print()
df6.to_csv(sys.stdout, sep="<")
print(df6)
print()
df7 = pd.read_table("veri5.txt")
print(df7)
df7.to_csv("yeni_veri3.csv", sep=":", na_rep="NULL")
print()
df8 = pd.read_table("veri.txt")
print(df8)
print()
df8.to_csv("yeni_veri4.csv", index=False, header=False)
print()
df9 = pd.read_table("veri6.txt")
print(df9)
print()
df9.to_csv("yeni_veri5.csv", index=False, header=False)
print()
df10 = pd.read_table("veri7.txt")
print(df10)
print()
df10.to_csv("yeni_veri6.csv", index=False,
            columns=["isim", "puan"])





