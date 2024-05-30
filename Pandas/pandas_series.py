
import pandas as pd
from pprint import pprint
import numpy as np
import matplotlib.pyplot as plt

#print(pd.__version__)

#calisan = ["mert", "demir", 32, "avukat", "niğde"]
#print(calisan)
#print(type(calisan))
#
#print("_"*50)
#
#seri = pd.Series(calisan)
#print(seri)
#print(type(seri))

#calisan = {
#    "isim": "kemal",
#    "soyisim": "erdem",
#    "yaş": 37,
#    "meslek": "şoför"
#}
#
#print(calisan)
#print(type(calisan))
#
#print("_"*50)
#
#seri = pd.Series(calisan)
#print(seri)
#print(type(seri))

#calisan = pd.Series(["serkan", "sevim", 42, "doktor"])
#print(calisan)
#print(type(calisan))
#
#print("_"*50)
#
#sayilar = pd.Series([18, 28, 38, 48])
#print(sayilar)
#print(type(sayilar))
#
#print("_"*50)
#
#sayilar2 = pd.Series([9, 19, 29, 39.9])
#print(sayilar2)
#print(type(sayilar2))
#
#print("_"*50)
#
#bool_degerler = pd.Series([True, False, True, False, False])
#print(bool_degerler)
#print(type(bool_degerler))

#calisan = pd.Series(data=["fatih", "koç", "yazılımcı", "samsun", 48],
#                    index=["isim", "soyisim", "meslek", "memleket", "yaş"])
#
#print(calisan)
#print(type(calisan))
#print()
#print(calisan.values)
#print()
#print(calisan.index)
#print()
#print(calisan.shape)
#print()
#print(calisan.ndim)
#print()
#print(calisan.size)
#print()
#print(len(calisan))
#print()
#print(calisan.dtype)
#print()
#print(calisan.dtypes)
#print()
#
#calisan.name = "korhan"
#print(calisan.name)

#calisan = pd.Series(data=["yalın", "tamer", "muhasebeci", "istanbul", 45],
#                    index=["isim", "soyisim", "meslek", "memleket", "yaş"])

#a = "isim" in calisan
#b = "soyisim" in calisan
#c = "okul" in calisan
#d = "ülke" in calisan
#e = 50 in calisan
#
#print(a, b, c, d, e)

#a = "adnan" in calisan.values
#b = "inanç" in calisan.values
#c = "muhasebeci" in calisan.values
#d = "istanbul" in calisan.values
#e = 45 in calisan.values
#
#print(a, b, c, d, e)

#pprint(calisan)

#sayilar = pd.Series([5, 8, 10, 13])
#print(sayilar)
#print(sayilar.sum())
#print(sayilar.mean())
#print(sayilar.product())

#ögrenci = pd.Series(data=["ümit", "doğan", "matematik", 12],
#                    index=["isim", "soyisim", "bölüm", "yaş"])
#
#print(ögrenci)
#print()
#print(ögrenci["isim"])
#print(ögrenci["soyisim"])
#print(ögrenci["bölüm"])
#print(ögrenci["yaş"])
#print()
#print(ögrenci[["isim", "soyisim"]])
#print()
#print(ögrenci[["bölüm", "yaş"]])
#print()
#print(type(ögrenci["isim"]))
#print(type(ögrenci[["isim", "soyisim", "bölüm", "yaş"]]))
#print()
#print(ögrenci[-1])
#print(ögrenci[0])
#print(ögrenci[[1, 2]])
#print("\n")
#print(ögrenci[0:3])
#print("\n")
#print(ögrenci[2:4])
#print("\n")
#print(ögrenci[-3:])
#print("\n")
#print()
#print(ögrenci["isim": "bölüm"])
#print("\n")
#print()
#print(ögrenci["soyisim": "yaş"])
#print("\n")
#print()
#print(ögrenci["bölüm": "yaş"])

#ögrenci = pd.Series(data=["kemal", "aydın", "fizik", 14],
#                    index=["isim", "soyisim", "bölüm", "yaş"])

#print(ögrenci.loc[["isim", "soyisim"]])
#print()
#print(ögrenci.loc[["bölüm", "yaş"]])
#print()
#print(ögrenci.loc["isim"])
#print()
#print(ögrenci.loc["soyisim"])
#print()
#print(ögrenci.loc["bölüm"])
#print()
#print(ögrenci.loc["yaş"])

#print(ögrenci.iloc[0])
#print()
#print(ögrenci.iloc[1])
#print()
#print(ögrenci.iloc[2])
#print()
#print(ögrenci.iloc[-1])
#print()
#print(ögrenci.iloc[[0, -1]])
#print()
#print(ögrenci.iloc[[1, 2]])
#print()
#print(ögrenci.loc[["yaş", "bölüm", "soyisim", "isim"]])
#print()
#print(ögrenci.iloc[[-1, -2, -3, -4]])

#ögrenci = pd.Series(data=["yalın", "akbulut", "edebiyat", 13],
#                    index=["isim", "soyisim", "bölüm", "yaş"])

#print(ögrenci)
#print()
#ögrenci["isim"] = "suat"
#print(ögrenci)
#print()
#ögrenci.iloc[-1] = 15
#print(ögrenci)
#print()
#ögrenci.loc["bölüm"] = "türkçe"
#print(ögrenci)
#print()
#ögrenci.loc[["isim", "soyisim"]] = "harun", "tabak"
#print(ögrenci)
#print()
#ögrenci.iloc[[2, 3]] = "kimya", 18
#print(ögrenci)
#print()
#ögrenci.drop("isim", inplace=True)
#print(ögrenci)
#print()
#ögrenci.drop(["soyisim", "bölüm"], inplace=True)
#print(ögrenci)
#print()
#ögrenci.drop("yaş", inplace=True)
#print(ögrenci)

#ögrenci = pd.Series(data=["emir", "kartal", "coğrafya"],
#                    index=["isim", "soyisim", "bölüm"])
#
#print(ögrenci)
#print()
#print(len(ögrenci))
#print(list(ögrenci))
#print(dict(ögrenci))
#print()
#print(sorted(ögrenci))
#print()
#print(min(ögrenci))
#print(max(ögrenci))

#students = [
#    {"isim": "Fatih", "soyisim": "Albayrak", "eposta": "fatih@gmail.com"},
#    {"isim": "Kamil", "soyisim": "Şener", "eposta": "kamil@gmail.com"},
#]
#
#df = pd.DataFrame(students)
#print(df)
#print(type(df))

#students = {
#    "isim": ["ömer", "tarık", "leyla", "neşe"],
#    "soyisim": ["bal", "koral", "eren", "güler"],
#    "eposta": ["ömerbal@gmail.com", "tarıkkoral@gmail.com", "leylaeren@gmail.com", "neşegüler@gmail.com"],
#    "yaş": [13, 15, 12, 14]
#}
#
#df = pd.DataFrame(students)
#print(df)
#print(type(df))
#print()
#print(df["eposta"])
#print()
#print(df[["eposta", "yaş"]])
#print()
#print(df.columns.tolist())
#print()
#print(df.iloc[0])
#print()
#print(df.iloc[-1])
#print()
#print(df.iloc[1]["eposta"])
#print()
#print(df["soyisim"].iloc[-1])
#print()
#print(df.iloc[2]["yaş"])
#print()
#print(df["isim"].iloc[2])
#df.index = df.index + 50
#print(df)
#print("_"*100)
#print(df.loc[51]["isim"])
#print()
#print(df.loc[53]["yaş"])
#print()
#print(df["soyisim"].loc[50])
#print()
#print(df["eposta"].loc[52])
#print()
#print(df.shape)

#seri = pd.Series([5.0, 6.0, 7.8, 9.2])
#print(seri)
#print("_"*50)
#
#seri2 = pd.Series([2.3, 12, 20, 23, 25, "selam", "xyz"])
#print(seri2)
#print("_"*50)
#
#seri3 = pd.Series(["hello", "python", 2, 4, 9.5, 12.7])
#print(seri3)
#print()
#seri_liste= seri3.tolist()
#print(seri_liste)
#print()
#print(type(seri3))
#print(type(seri_liste))
#print("_"*50)

#seri4 = pd.Series([15, 20, 25, 30])
#seri5 = pd.Series([3, 4, 5, 6])
#
#seriler_toplam = seri4 + seri5
#seriler_fark = seri4 - seri5
#seriler_carpim = seri4 * seri5
#seriler_bölüm = seri4 / seri5
#
#print(f"serilerin toplamı = {seriler_toplam} "
#      f"serilerin farkı = {seriler_fark} "
#      f"serilerin çarpımı = {seriler_carpim} "
#      f"serilerin bölümü = {seriler_bölüm}")
#
#print("_"*50)
#
#seri6 = pd.Series([11, 21, 25, 28, 37, 39, 46, 47])
#seri7 = pd.Series([8, 10, 33, 35, 37, 39, 55, 42])

#print(seri6 == seri7)
#print()
#print(seri6 > seri7)
#print()
#print(seri6 < seri7)
#print()
#print(seri6 != seri7)
#
#print("_"*50)
#
#sözlük = {"a": 20, "b": 30, "c": 40, "d": 50, "e": 60}
#print(sözlük)
#print(type(sözlük))
#seri8 = pd.Series(sözlük)
#print(seri8)
#print(type(seri8))
#print("_"*50)

#array = np.array([3, 5, 9, 14, 20, 25])
#print(array)
#print(type(array))
#print()
#
#seri9 = pd.Series(array)
#print(seri9)
#print(type(seri9))
#print("_"*50)
#
#seri10 = pd.Series(["30", "33", "38", "46", "57", "python"])
#print(seri10)
#print()
#
#numerik_seri1 = pd.to_numeric(seri10, errors="coerce") # coerce string ifadeyi NaN olarak verir
#print(numerik_seri1)
#print()
#
#numerik_seri2 = pd.to_numeric(seri10, errors="ignore") # ignore string ifadeyi olduğu gibi verir
#print(numerik_seri2)
#print()

#try:
#      numerik_seri3 = pd.to_numeric(seri10, errors="raise") # raise string ifade ile karşılaşınca hata verir
#      print(numerik_seri3)
#
#except:
#      print("patladık!!!")
#
#print("_"*50)
#
#
#seri11 = pd.Series(["java", "23.5", "52", "40", "html"])
#print(seri11)
#print()
#
#numerik_seri4 = pd.to_numeric(seri11, errors="coerce")
#print(numerik_seri4)
#print()
#
#numerik_seri5 = pd.to_numeric(seri11, errors="ignore")
#print(numerik_seri5)
#print()

#try:
#      numerik_seri6 = pd.to_numeric(seri11, errors="raise")
#      print(numerik_seri6)
#
#except:
#      print("patladık!!")
#print("_"*50)
#
#seri12 = pd.Series(["10", "20", "selam", "merhaba", "50"])
#print(seri12)
#print()
#print(seri12.values)
#print()
#print(type(seri12))
#print("\n")

#np_seri = np.array(seri12)
#print(np_seri)
#print(type(np_seri))
#print("_"*50)
#
#seri13 = pd.Series([["mavi", "beyaz", "yeşil"],
#                    ["sarı", "siyah"],
#                    ["kırmızı"]])
#print(seri13)
#print(type(seri13))
#print()
#tek_seri1 = seri13.apply(pd.Series).stack().reset_index(drop=True)
#print(tek_seri1)
#print("_"*50)
#
#seri14 = pd.Series([["fizik", "matematik", "kimya", "biyoloji"],
#                    ["edebiyat", "türkçe", "coğrafya"],
#                    ["tarih", "felsefe"],
#                    ["ingilizce"]])

#print(seri14)
#print(type(seri14))
#tek_seri2 = seri14.apply(pd.Series).stack().reset_index(drop=True)
#print(tek_seri2)
#
#seri15 = pd.Series([["fransa", "almanya"],
#                    ["meksika", "kolombiya", "uruguay", "paraguay"],
#                    ["kore", "çin", "japonya"],
#                    ["isveç", "norveç", "finlandiya", "hollanda", "belçika"]])
#
#print(seri15)
#print(type(seri15))
#tek_seri3 = seri15.apply(pd.Series).stack().reset_index(drop=True)
#print(tek_seri3)
#print("_"*50)

#seri16 = pd.Series([324, 35, 567, 76, 87, 13])
#artarak1 = seri16.sort_values(ascending=True).reset_index(drop=True)
#print(artarak1)
#print()
#azalarak1 = seri16.sort_values(ascending=False).reset_index(drop=True)
#print(azalarak1)
#print("_"*50)
#
#seri17 = pd.Series(["css", "html", "php", "java", "ruby"])
#artarak2 = seri17.sort_values(ascending=True).reset_index(drop=True)
#print(artarak2)
#print()
#azalarak2 = seri17.sort_values(ascending=False).reset_index(drop=True)
#print(azalarak2)
#print("_"*50)
#
#seri18 = pd.Series([12, 14, 16, 17, 19])
#print(seri18._append(pd.Series([100, 200, "istanbul", "ankara"]), ignore_index=True))
#print("_"*50)

#seri19 = pd.Series(["ali", "veli", "mehmet"])
#print(seri19._append(pd.Series(["ahmet", "hasan", 333, 555, 121, 245, 6789]),
#                     ignore_index=False))
#
#print("_"*50)
#
#seri20 = pd.Series([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
#alt_küme1 = seri20[seri20 > 10].reset_index(drop=True)
#print(alt_küme1)
#print()
#alt_küme2 = seri20[seri20 != 5].reset_index(drop=True)
#print(alt_küme2)
#print()
#alt_küme3 = seri20[seri20 < 7].reset_index(drop=True)
#print(alt_küme3)
#alt_küme4 = seri20[seri20 % 2 == 0].reset_index(drop=True)
#print(alt_küme4)
#alt_küme5 = seri20[seri20 % 5 == 0].reset_index(drop=True)
#print(alt_küme5)
#print("_"*50)

#seri21 = pd.Series(data=[150, 250, 300, 350, 400],
#                   index=["A", "E", "C", "B", "D"])
#print(seri21)
#print()
#yeni_seri1 = seri21.reindex(index=["A", "B", "C", "D", "E"])
#print(yeni_seri1)
#print("_"*50)
#
#seri22 = pd.Series(data=["ilkokul", "ortaokul", "lise", "üniversite", "yüksek lisans"],
#                   index=["a", "b", "c", "d", "e"])
#print(seri22)
#print()
#yeni_seri2 = seri22.reindex(index=["e", "d", "c", "b", "a"])
#print(yeni_seri2)
#
#seri23 = pd.Series(data=["mavi", "turuncu", "kırmızı", "pembe", "mor", "sarı", "kahverengi"],
#                   index=[100, 200, 300, 400, 500, 600, 700])
#print(seri23)
#print()
#yeni_seri3 = seri23.reindex(index=[500, 200, 700, 400, 100, 300, 600])
#print(yeni_seri3)
#print("_"*50)

#seri24 = pd.Series([2, 5, 7, 8, 10, 20, 22])
#print(f"ortalaması = {seri24.mean().round(3)}")
#print(f"standart sapması = {seri24.std().round(2)}")
#print(f"varyansı = {seri24.var().round(4)}")
#print("_"*50)
#
#
#seri25 = pd.Series(np.random.randint(1, 5, 10))
#print(seri25)
#print()
#print(seri25.value_counts())
#print("_"*50)
#
#seri26 = pd.Series(list("405967905"))
#print(seri26)
#cikarilacaklar_index = [2, 5, 7, 8]
#sonuc = seri26.take(cikarilacaklar_index)
#print(sonuc)
#print()

#seri27 = pd.Series(data=["almanya", "ispanya", "fransa", "ingiltere", "portekiz", "çin", "kore", "japonya", "özbekistan"],
#                   index=["a", "b", "c", "d", "e", "f", "g", "h", "j"])
#
#print(seri27.reset_index(drop=True))
#print()
#sonuc = seri27.take([0, 1, 2])
#print(sonuc)
#print()
#
#seri28 = pd.Series(data=["doktor", "yazılımcı", "avukat", "mühendis", "öğretmen", "aşçı", "şoför"])
#
#print(seri28)
#print()
#sonuc = seri28.take([0, 2, 4])
#print(sonuc)
#
#seri29 = pd.Series(data=["sarı", "beyaz", "mavi", "kırmızı", "siyah", "mor", "pembe", "eflatun", "turuncu", "lacivert", "turkuaz"])
#
#print(seri29)
#print()
#sonuc = seri29.take([1, 2, 5, 7, 8, 9])
#print(sonuc)
#print("_"*50)

#dizi1 = pd.Series([19, 29, 39, 49, 59, 69, 79, 89, 99, 109, 119, 129, 139])
#dizi2 = pd.Series([2, 3, 6, 7, 10])
#
#liste1 = []
#
#for i in dizi2:
#    liste1.append(dizi1.iloc[i])
#print(liste1)
#
#dizi3 = pd.Series(["yeşil", "turuncu", "eflatun", "kırmızı", "mavi", "beyaz", "sarı", "turkuaz", "siyah", "kahverengi", "mor", "pembe"])
#print(dizi3)
#print()
#dizi4 = pd.Series([3, 8, 10, 11])
#print(dizi4)
#print()
#
#liste2 = []
#
#for i in dizi4:
#    liste2.append(dizi3.iloc[i])
#
#print(liste2)

#dizi5 = pd.Series(range(20, 40, 2))
#print(dizi5)
#dizi6 = pd.Series(list("abcdefghjk"))
#print(dizi6)
#print()
#dizi7 = pd.Series(list("ABCDEFGHJK"))
#print(dizi7)
#
#df = pd.concat([dizi5, dizi6, dizi7], axis=0, ignore_index=True)
#print(df)
#print("_"*50)
#
#dizi8 = pd.Series(range(100, 140, 5))
#print(dizi5)
#dizi9 = pd.Series(list("lmnoöprs"))
#print(dizi6)
#print()
#dizi10 = pd.Series(list("LMNOÖPRS"))
#print(dizi7)

#df = pd.concat([dizi8, dizi9, dizi10], axis=1)
#print(df.to_string())
#print("_"*50)
#
#dizi11 = pd.Series([10, 20])
#dizi12 = pd.Series([15, 25])
#
#öklid_uzaklik = np.linalg.norm(dizi11 - dizi12)
#print(f"iki seri arasındaki öklid uzaklığı = {öklid_uzaklik}")
#print("_"*200)
#

data = {
    "şehir": ["adana", "izmir", "istanbul", "ankara", "adana", "izmir"],
    "cinsiyet": ["erkek", "kadın", "kadın", "kadın", "erkek", "erkek"],
    "yaş": [43, 46, 43, 57, 46, 57],
    "el": ["sağ", "sol", "sol", "sağ", "sol", "sağ"]
}

df = pd.DataFrame(data)
print(df)
print()
capraz_tablo1 = pd.crosstab(df["şehir"], df["cinsiyet"])
print(capraz_tablo1)
print()
capraz_tablo2 = pd.crosstab(df["yaş"], df["el"])
print(capraz_tablo2)
print()
capraz_tablo3 = pd.crosstab(df["cinsiyet"], df["yaş"], margins=True)
print(capraz_tablo3)
print()
capraz_tablo4 = pd.crosstab(df["şehir"], df["el"], margins=True)
print(capraz_tablo4)
print()
capraz_tablo5 = pd.crosstab([df["şehir"], df["cinsiyet"]],
                            [df["el"], df["yaş"]], margins=True)
print(capraz_tablo5)
print()
capraz_tablo6 = pd.crosstab(df["şehir"], df["cinsiyet"], normalize=True) * 100
print(capraz_tablo6)
print()
capraz_tablo7 = pd.crosstab(df["cinsiyet"], df["el"], normalize=True) * 100
print(capraz_tablo7)
print()

print("_"*100)

data2 = {
    "isim": ["harun", "selim", "akın", "harun", "selim", "akın"],
    "soyisim": ["serin", "tan", "durmaz", "serin", "tan", "durmaz"],
    "vize": [50, 60, 30, 40, 70, 100],
    "final": [40, 20, 30, 80, 90, 50],
    "yaş": [18, 22, 25, 17, 23, 21]
}

df2 = pd.DataFrame(data2)
print(df2)
print()
capraz_tablo8 = pd.crosstab(df2["isim"], df2["soyisim"],
                            values=df2["vize"], aggfunc=np.sum)
print(capraz_tablo8)
print()
capraz_tablo9 = pd.crosstab(df2["soyisim"], df2["isim"],
                            values=df2["final"], aggfunc=np.average)
print(capraz_tablo9)
print()
capraz_tablo10 = pd.crosstab(df2["isim"], df2["soyisim"],
                            values=df2["yaş"], aggfunc=np.product)
print(capraz_tablo10)

print("_"*1000)





#obje = pd.Series([44, "abc", 5.7, "python"])
#print(obje)
#print()
#print(obje[0])
#print()
#print(obje[3])
#print()
#print(obje.values)
#print()
#print(type(obje.values))
#print()

#obje2 = pd.Series(["java", 23, 40, 10.5, "hello"],
#                  index=["a", "b", "c", "d", "e"])
#
#print(obje2)
#print()
#print(obje2["c"])
#print()
#print(obje2["e"])
#print()
#print(obje2.index)
#print("\n\n")
#
#puan = {"metin": 30, "samet": 60, "ercan": 50}
#print(type(puan))
#nt = pd.Series(puan)
#print(nt)
#print(type(nt))
#print()
#print(nt["ercan"])
#print()
#print(nt["metin"])
#print()
#print(nt[nt > 40])
#print()
#print(nt[nt < 35])
#print()
#print(nt < 55)
#print()
#print(nt != 30)
#print()
#print(nt == 50)
#print()
#nt["metin"] = 75
#nt["ercan"] = 95
#nt["samet"] = 85
#print(nt)
#print()
#nt[nt < 96] = 98
#print(nt)
#print()
#nt[nt > 90] = 58
#print(nt)
#print()
#nt[nt == 58] = 43
#print(nt)
#print()
#print("Metin".lower() in nt)
#print()
#print("ERCAN".lower() in nt)
#print()
#print("samet" not in nt)
#print()
#print("keremcan" not in nt)
#print()
#print(nt / 2)
#print()
#print(nt * 5)
#print()
#nt["hasan"] = pd.NA
#nt["erdem"] = np.nan
#nt["vedat"] = None
#print(nt)
#print()
#print(nt.isnull())
#print()
#print(nt.notnull())

games = pd.read_csv("vgsalesGlobale.csv")
print(games.head().to_string())
print()
print(games.dtypes)
print()
print(type(games))
print()
print(games["Genre"].describe())
print()
print(games["Genre"].value_counts())
print()
print(games["Genre"].value_counts(normalize=True))
print()
print(games["Genre"].value_counts(normalize=True, ascending=False))
print()
print(games["Genre"].value_counts(normalize=True, ascending=True))
print()
print(type(games["Genre"].value_counts()))
print()
print(games["Genre"].tail())
print()
print(games["Genre"].unique())
print()
print(games["Genre"].nunique())
print()
print(pd.crosstab(games["Genre"], games["Year"]))
print()
print(pd.crosstab(games["Rank"], games["Year"]))
print()
print(games["Global_Sales"].describe())
print()
print(games["Year"].describe())
print()
print(games["Publisher"].describe())
print()
print(games["Name"].describe())
print()
print(games["Rank"].describe())
print()
print(games["Rank"].min())
print()
print(games["Rank"].max())
print()
print(int(games["Rank"].mean()))
print()
print(games["Global_Sales"].value_counts().to_string())
print()
print(games["Name"].value_counts().to_string())
print()
print(games["Year"].value_counts(ascending=True).to_string())
print()
print(games["EU_Sales"].value_counts(ascending=True).to_string())
print()
print(games["Platform"].value_counts(ascending=True).to_string())
print()
print(games["NA_Sales"].value_counts().head(10))
print()
#print(games["NA_Sales"].head(10).plot(kind="hist"))
#plt.show()
#print()
#print(games["Genre"].value_counts())
#print()
#games["Genre"].value_counts(normalize=True, ascending=True).plot(kind="bar")
#plt.show()

#print(games["Publisher"].value_counts().head(10))
#print()
#games["Publisher"].value_counts(ascending=False).head(10).plot(kind="barh")
#plt.show()

#print(games["Name"].value_counts().head(10))
#print()
#games["Name"].value_counts(ascending=False).head(10).plot(kind="bar")
#plt.show()















#def fonk(a, b, c):
#      if a * b + c > 200:
#            return True
#      else:
#            return False
#
#seri = pd.Series([4, 6, 8])
#
#print(seri.apply(fonk, args=[30, 40]))

#def fonk(a, b, c, d):
#      if a * b > c * d:
#            return True
#      else:
#            return False
#
#seri = pd.Series([2, 3, 5, 6])
#print(seri.apply(fonk, b=500, c=30, d=60))

#def fonk(a, b, c):
#      if len(a) > len(b) and len(a) > len(c):
#            return True
#      else:
#            return False
#
#seri = pd.Series(["python", "javascript", "php"])
#print(seri.apply(fonk, b="yazılım", c="software"))














