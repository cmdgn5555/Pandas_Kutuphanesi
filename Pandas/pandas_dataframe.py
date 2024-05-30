
import pandas as pd
import numpy as np
import openpyxl
from pprint import pprint

ögrenciler = {"isim": ["ali", "cemil", "canan", "elif", "özge", "tarık", "kemal", "ayten", "aslı", "harun"],
              "vize": [50, 55, 70, np.nan, 40, 30, 15, np.nan, 35, 20],
              "final": [85, 70, 60, 30, 50, 55, 75, 100, 65, 90],
              "cinsiyet": ["erkek", "erkek", "kadın", "kadın", "kadın", "erkek", "erkek", "kadın", "kadın", "erkek"],
              "dersler": ["türkçe", "matematik", "tarih", "matematik", "türkçe", "türkçe", "tarih", "tarih", "matematik", "matematik"],
              "hobiler": ["spor", "seyahat", "kitap okuma", "spor", "spor", "kitap okuma", "seyahat", "kitap okuma", "spor", "seyahat"],
              "memleket": ["ankara", "izmir", "bursa", "izmir", "bursa", "ankara", "ankara", "izmir", "bursa", "bursa"]}

indeksler = ["a", "b", "c", "d", "e", "f", "g", "h", "j", "k"]

df = pd.DataFrame(data=ögrenciler, index=indeksler)
print(df)
print("_"*50)
print(df.info())
print("_"*50)
print(df.iloc[0:5, 0:2])
print("_"*50)
print(df[["final", "cinsiyet"]])
print("_"*50)
print(df.iloc[[2, 3, 6, 7], [0, 1, 2]])
print("_"*50)
print(df.loc[["a", "b", "j", "k"], ["vize", "final"]])
print("_"*50)
print(df[df["final"] > 50])
print("_"*50)
print(df[df["vize"] <= 30])
print("_"*50)
print(df[df["cinsiyet"] != "erkek"])
print("_"*50)
print(df[df["cinsiyet"] == "erkek"])
print("_"*50)
print(df.shape)
print("_"*50)
print(f"satır sayısı = {df.shape[0]}")
print(f"sütun sayısı = {df.shape[1]}")
print("_"*50)
print(df[df["final"].between(40, 60)])
print("_"*50)
print(df[df["vize"].between(60, 100)])
print("_"*50)
print(df[(df["cinsiyet"] == "erkek") & (df["final"] > 70)])
print("_"*50)
print(df[(df["cinsiyet"] == "kadın") | (df["vize"] < 25)])
print("_"*50)
print(df[(df["vize"] > 30) & (df["final"] < 80)])
print("_"*50)
print(df[(df["vize"] < 50) | (df["final"] > 90)])
print()
print("_"*50)
df.loc["d", "vize"] = 95
print(df)
print("_"*50)
df.loc["h", "vize"] = 75
print(df)
print("_"*50)
df.loc["a", ["isim", "cinsiyet"]] = "mehmet", "erkek"
print(df)
print("_"*50)
df.loc["j", ["isim", "vize", "final", "cinsiyet"]] = "fatih", 100, 100, "erkek"
print(df)
print("_"*50)
df.loc["k", ["isim", "vize", "final", "cinsiyet"]] = "saliha", 80, 80, "kadın"
print(df)
print("_"*50)
print(df["final"].mean())
print("_"*50)
print(df["vize"].mean())
print("_"*50)
print(df["final"].max() + df["vize"].min())
print("_"*50)
print(df["final"].median() - df["vize"].median())
print("_"*50)
print(df["final"].sum() - df["vize"].sum())
print("_"*50)
df["cinsiyet"] = df["cinsiyet"].map({"erkek": "male", "kadın": "female"})
print(df)
print("_"*50)
df["dersler"] = df["dersler"].map({"türkçe": "ingilizce", "matematik": "geometri", "tarih": "coğrafya"})
print(df)
print("_"*50)
df["hobiler"] = df["hobiler"].map({"spor": "futbol", "seyahat": "sinema", "kitap okuma": "tiyatro"})
print(df)
print("_"*50)
df["memleket"] = df["memleket"].map({"ankara": "adana", "izmir": "edirne", "bursa": "mersin"})
print(df)
print("_"*50)
df["isim"] = df["isim"].replace("canan", "meltem")
print(df)
print("_"*50)
df["cinsiyet"] = df["cinsiyet"].replace(["male", "female"], ["erkek", "bayan"])
print(df)
print("_"*50)
df["memleket"] = df["memleket"].replace(["adana", "edirne", "mersin"], ["trabzon", "tokat", "tunceli"])
print(df)
print("_"*50)
df["renkler"] = ["mor", "sarı", "yeşil", "pembe", "mavi", "siyah", "kırmızı", "beyaz", "turuncu", "turkuaz"]
print(df)
print("_"*50)
df["yaşlar"] = [26, 22, 25, 28, 21, 24, 32, 30, 33, 35]
print(df)
print("_"*50)
df.columns = ["İsimler", "Vize", "Final", "Cinsiyet", "Dersler", "Hobiler", "Memleket", "Renkler", "Yaşlar"]
print(df)
print("_"*50)
df2 = pd.DataFrame({"column1": [100, 200, 300],
                    "column2": [400, 500, 600],
                    "column3": [700, 800, 900]})

print(df2)
print()
df2.columns = ["SÜTUN 1", "SÜTUN 2", "SÜTUN 3"]
print(df2)
print("_"*50)

df.to_csv("yeni_dosya.csv", sep="\t", index=False)
yeni_df = pd.read_csv("yeni_dosya.csv")
print(yeni_df)

try:
    df2.to_excel("yeni_dosya_2.xlsx", index=True)
    yeni_df2 = pd.read_csv("yeni_dosya_2.xlsx")
    print(yeni_df2)

except:
    print("dosya okunamadı...")
print("_"*50)

df3 = pd.DataFrame({"isim": ["hakan", "orhan", "caner", "harun", "serkan",
                             "ayhan", "kemal", "mehmet", "tolga", "recep"],

                    "şehir": ["balıkesir", "balıkesir", "bursa", "bursa", "antalya",
                              "antalya", "antalya", "ankara", "ankara", "ankara"]})

print(df3)
print()
df3_group = df3.groupby(["şehir"]).size().reset_index(name="kişi sayısı")
print(df3_group)

print("_"*50)

df4 = pd.DataFrame({"şehirler": ["roma", "torino", "venedik", "floransa", "madrid", "barcelona",
                                 "valencia", "sevilla", "manchester", "londra", "liverpool", "birmingham"],

                    "ülkeler": ["italya", "italya", "italya", "italya", "ispanya", "ispanya",
                                "ispanya", "ispanya", "ingiltere", "ingiltere", "ingiltere", "ingiltere"]})

print(df4)
print()
df4_group = df4.groupby(["ülkeler"]).size().reset_index(name="şehir sayısı")
print(df4_group)

print("_"*50)

df5 = pd.DataFrame({"futbolcular": ["modric", "bellingham", "mbappe", "dembele", "haaland", "foden",
                                 "kane", "müller", "pogba", "chiesa", "pedri", "rapinha"],

                    "takımlar": ["real madrid", "real madrid", "psg", "psg", "manchester city", "manchester city",
                                "bayern münih", "bayern münih", "juventus", "juventus", "barcelona", "barcelona"]})

print(df5)
print()
df5_group = df5.groupby(["takımlar"]).size().reset_index(name="futbolcu sayısı")
print(df5_group)
print("_"*50)

tit_csv = pd.read_csv("titanic.csv")

pd.set_option("display.max_columns", 4)
print("_"*50)
pd.set_option("display.max_rows", 1000)
print(tit_csv)
print("_"*250)

df6 = pd.DataFrame({"isim": ["ali", "veli", np.nan, "mehmet"],
        "soyisim": ["akyol", pd.NA, "akın", "şener"],
       "yaş": [None, 28, 34, 45],
        "memleket": ["istanbul", "edirne", np.nan, pd.NA]})

print(df6)
print("_"*50)

df6.fillna("boş değer", inplace=True)
print(df6)
print("_"*50)

df7 = pd.DataFrame({"ülkeler": ["almanya", "fransa", "ispanya", "italya", "ingiltere", "amerika"],
                    "başkentler": ["berlin", "paris", "madrid", "roma", "londra", "washington"],
                    "nüfus": [12000000, 17500000, 10000000, 8000000, 7500000, 13500000]})

print(df7)
print("_"*50)

df7.reset_index(inplace=True)
print(df7)
print("_"*50)

df7.set_index("ülkeler", inplace=True)
print(df7)
print("_"*50)
print(df7.index.values)
print("_"*50)

df8 = pd.DataFrame({"isim": ["ali", "veli", np.nan, "mehmet", None, "rıza", None],
        "soyisim": ["akyol", pd.NA, "akın", "şener", pd.NA, np.nan, "ersen"],
       "yaş": [None, 28, 34, 45, None, 20, 30],
        "memleket": ["istanbul", "edirne", np.nan, pd.NA, "ankara", "izmir", "adana"]})

print(df8)
print()
print(df8.info())
print("_"*50)
print(df8.isnull().values.sum())
print("_"*50)
print(df8.notnull().values.sum())

df9 = pd.DataFrame({"col1": [1050, 1150, 1250, 1350, 1450, 1550, 1650, 1750, 1850, 1950],
                    "col2": [2050, 2150, 2250, 2350, 2450, 2550, 2650, 2750, 2850, 2950],
                    "col3": [3050, 3150, 3250, 3350, 3450, 3550, 3650, 3750, 3850, 3950],
                    "col4": [4050, 4150, 4250, 4350, 4450, 4550, 4650, 4750, 4850, 4950]})

print(df9)
print("_"*50)

#df9.drop(df9.index[[2, 4]], inplace=True)
#print(df9)
#print("_"*50)

#df9.drop(df9.columns[[0, 2]], inplace=True, axis=1)
#print(df9)

#df9.drop(df9.index[5], inplace=True, axis=0)
#print(df9)

#df9.drop(df9.columns[1], inplace=True, axis=1)
#print(df9)

#df9.drop(df9.index[[3, 4, 5, 6]], inplace=True, axis=0)
#print(df9)

#df9.drop(df9.columns[[0, 1, 2]], inplace=True, axis=1)
#print(df9)

df10 = pd.DataFrame({"öğrenciler": ["hasan", "kemal", "tarık", "can", "suat", "sevgi", "selin", "osman", "merve", "emel", "şener", "kenan", "halil"],
                    "not": [40, 40, 40, 40, 65, 65, 65, 65, 90, 90, 90, 90, 90]})

print(df10)
print("_"*50)

#sırala = df10.sort_values(["not", "öğrenciler"], ascending=[False, False])
#print(sırala)

#sırala = df10.sort_values(["not", "öğrenciler"], ascending=[True, False])
#print(sırala)

#sırala = df10.sort_values(["not", "öğrenciler"], ascending=[False, True]).reset_index(drop=True)
#print(sırala)

#liste = [["sütun1", "sütun2", "sütun3"], [10, 20, 30], [40, 50, 60], [70, 80, 90]]
#print(liste)
#print()
#basliklar = liste.pop(0)
#print(basliklar)
#print()
#print(liste)
#print()
#
#df11 = pd.DataFrame(data=liste, columns=basliklar, index=["bir", "iki", "üç"])
#print(df11)

liste = [["selim", "başer", 30, "denizli"],
         ["fatma", "yılmaz", 33, "bilecik"],
         ["hülya", "inal", 41, "ordu"],
         ["isim", "soyisim", "yaş", "memleket"]]
print(liste)
print()
sütunlar = liste.pop(-1)
print(sütunlar)
print()

df11 = pd.DataFrame(data=liste, index=["bir", "iki", "üç"], columns=sütunlar)
print(df11)
print("_"*50)

veri = {"isim": ["enes", "emel", "eren", "kenan", "suzan", "nil"],
        "puan": [85, 45, 90, 60, 55, 70],
        "spor": ["futbol", "bale", "basketbol", "kaykay", "tenis", "hentbol"],
        "cinsiyet": ["erkek", "kadın", "erkek", "erkek", "kadın", "kadın"]}

dataframe1 = pd.DataFrame(veri)
print(dataframe1)
print()
dataframe2 = pd.DataFrame(veri, columns=["isim", "cinsiyet", "puan", "spor", "yaş"],
                          index=["bir", "iki", "üç", "dört", "beş", "altı"])
print(dataframe2.to_string())
print()
print(dataframe2["spor"])
print()
print(dataframe2["isim"])
sütunlar1 = ["cinsiyet", "puan"]
print(dataframe2[sütunlar1])
print()
sütunlar2 = ["isim", "spor", "yaş"]
print(dataframe2[sütunlar2])
print("_"*100)

print(dataframe2.loc["üç"])
print()
pprint(dataframe2.loc[["bir", "iki"]])
print()
dataframe2["yaş"] = [18, 19, 17, 22, 20, 21]
print(dataframe2.to_string())
print()
dataframe2["memleket"] = ["ankara", "erzincan", "mersin", "afyon", "bursa", "artvin"]
print(dataframe2.to_string())
print()
dataframe2["gecenler"] = dataframe2["puan"] > 65
print(dataframe2.to_string())
print()
dataframe2["kalanlar"] = dataframe2["puan"] < 50
print(dataframe2.to_string())
print()
dataframe2["iki katı"] = dataframe2["puan"] * 2
print(dataframe2.to_string())
print()
del dataframe2["gecenler"]
print(dataframe2.to_string())
print()
del dataframe2["kalanlar"]
print(dataframe2.to_string())
print()
del dataframe2["iki katı"]
print(dataframe2.to_string())
print()
print("_"*200)

notlar = {"edebiyat": {"murat": 80, "onur": 65, "halil": 70},
          "tarih": {"murat": 90, "onur": 75, "halil": 50},
          "geometri": {"murat": 60, "onur": 95, "halil": 85}}

grades = pd.DataFrame(notlar)
print(grades.to_string())
print()
grades = grades.transpose()
print(grades)
print()
grades.index.name = "dersler"
grades.columns.name = "isimler"
print(grades)
print()
print(grades.values)
print()
print(grades.value_counts())
print()


























