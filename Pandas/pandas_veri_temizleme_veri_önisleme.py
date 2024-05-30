
import pandas as pd
import numpy as np

veri = pd.DataFrame({"a": ["beş", "altı", "beş", "altı", "beş", "altı"],
                     "b": [2, 2, 3, 4, 3, 4]})

print(veri)
print()
print(veri.duplicated())
print()
print(veri.drop_duplicates())
print()
veri["c"] = range(10, 16)
print(veri)
print()
print(veri.duplicated("a"))
print()
print(veri.duplicated("b"))
print()
print(veri.duplicated("a", keep="last"))
print()
print(veri.duplicated("b", keep="last"))
print()
print(veri.duplicated(["a", "b"], keep="last"))
print("_"*500)

veri2 = pd.DataFrame({"isim": ["mert", "canberk", "arda", "belma", "selen"],
                      "soyisim": ["boz", "delen", "koza", "ay", "aslan"],
                      "göbek_adı": ["hasan", "alp", "erdem", "cemre", "berna"],
                      "puan": [40, 60, 50, 90, 70]})

print(veri2)
print()

sınıf = {"Mert": "B", "Canberk": "B", "Arda": "B", "Belma": "C", "Selen": "C"}
memleket = {"MERT": "Bolu", "CANBERK": "Ankara", "ARDA": "Konya", "BELMA": "Mersin", "SELEN": "İstanbul"}
vize = {"Boz": 25, "Delen": 45, "Koza": 85, "Ay": 55, "Aslan": 95}
final = {"BOZ": 43, "DELEN": 62, "KOZA": 78, "AY": 84, "ASLAN": 97}


ad1 = veri2["isim"].str.capitalize()
print(ad1)
print()

veri2["şube"] = ad1.map(sınıf)
print(veri2)
print()

ad2 = veri2["isim"].str.upper()
print(ad2)
print()

veri2["doğduğu il"] = ad2.map(memleket)
print(veri2)
print()

soyad1 = veri2["soyisim"].str.capitalize()
print(soyad1)
print()

veri2["vize_notları"] = soyad1.map(vize)
print(veri2)
print()

soyad2 = veri2["soyisim"].str.upper()
print(soyad2)
print()

veri2["final_notları"] = soyad2.map(final)
print(veri2)
print()
print("_"*500)

nt = pd.Series([20, 65, 35, 95, 100, 15, 35, 50,
                15, 32, 44, 56, 78, 93, 12, 16, 77, 73])
print(nt)
print()
nt.replace(20, np.nan, inplace=True)
print(nt)
print()
nt.replace([15, 32, 44, 56, 78],
           [None, pd.NA, np.nan, 0, 1],
           inplace=True)
print(nt)
print()
nt.replace({93: 92, 12: 11, 16: "selam"}, inplace=True)
print(nt)
print()
print("_"*500)

df = pd.DataFrame(data=np.arange(12).reshape(3, 4),
                  index=[0, 1, 2],
                  columns=["ege", "onur", "yeliz", "sezen"])

print(df)
print()
seri = pd.Series(["one", "two", "three"])
df.index = df.index.map(seri)
print(df)
print()
df.rename(index=str.title, columns=str.upper, inplace=True)
print(df)
print()
df.rename(index={"One": "five"}, columns={"EGE": "cenk"},
          inplace=True)
print(df)
print("_"*500)

df2 = pd.DataFrame(data=np.arange(12).reshape(4, 3),
                  index=[0, 1, 2, 3],
                  columns=["ALMANYA", "FRANSA", "HOLLANDA"])

print(df2)
print()
seri1 = pd.Series(["bir", "iki", "üç", "dört"])
df2.index = df2.index.map(seri1)
print(df2)
print()
df2.rename(index=str.capitalize, columns=str.lower, inplace=True)
print(df2)
print()
df2.rename(index={"Bir": "0N", "Iki": "YİRMİ", "Üç": "OTUZ", "Dört": "KIRK"},
           columns={"almanya": "ADANA", "fransa": "SAMSUN", "hollanda": "BURSA"},
           inplace=True)
print(df2)
print("_"*500)

df3 = pd.DataFrame(data=np.arange(100, 124).reshape(6, 4),
                  index=[0, 1, 2, 3, 4, 5],
                  columns=["mor", "sarı", "pembe", "eflatun"])

print(df3)
print()
print(df3.index)
print()
seri2 = pd.Series(["renk1", "renk2", "renk3", "renk4", "renk5", "renk6"])
df3.index = df3.index.map(seri2)
print(df3)
print()
df3.rename(index=str.upper, columns=str.title, inplace=True)
print(df3)
print()
df3.rename(index={"RENK1": "Color1", "RENK2": "Color2", "RENK3": "Color3"},
           columns={"Mor": "KIRMIZI", "Sarı": "BEYAZ", "Pembe": "LACİVERT", "Eflatun": "YEŞİL"},
           inplace=True)

print(df3)












