import pandas as pd
import numpy as np

veriler = {"isim": ["ayşe", "ali", "merve", "ahmet", "mehmet", "berna", "selma", "oğuz", "onur", "özlem"],
           "yıllık izin": [20, 23.5, 32, np.nan, 19, 13.5, 28, np.nan, 10, 12],
           "çalışma yılı": [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
           "cinsiyet": ["kadın", "erkek", "kadın", "erkek", "erkek", "kadın", "kadın", "erkek", "erkek", "kadın"]}

indeksler = ["a", "b", "c", "d", "e", "f", "g", "h", "k", "m"]

df = pd.DataFrame(data=veriler, index=indeksler)
print(df)
print("_"*50)

#df[["yıllık izin", "çalışma yılı"]] = df[["çalışma yılı", "yıllık izin"]]
#print(df)
#print("_"*50)

#df[["isim", "cinsiyet"]] = df[["cinsiyet", "isim"]]
#print(df)
#print("_"*50)

#df["isim"] = df["çalışma yılı"]
#print(df)
#print("_"*50)
#
#df["yıllık izin"] = df["cinsiyet"]
#print(df)

seri = pd.Series(data=[5, 10, 15], index=list("abc"))
print(seri)
print()
print(seri.a)
print(seri.b)
print(seri.c)
print("_"*50)

df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]})
print(df)
print()
df.iloc[-1] = {"a": 55, "b": 66, "c": 77}
print(df)
print()
df.iloc[0] = {"a": 22, "b": 33, "c": 44}
print(df)
print("_"*50)

df1 = pd.DataFrame(data=np.random.rand(10, 6),
                   index=list("abcdefghmn"),
                   columns=list("ABCDEF"))

print(df1)
print()
dilimle1 = df1.loc[["a", "e", "m"], :]
print(dilimle1)
print()
dilimle2 = df1.loc["c": "h", :]
print(dilimle2)
print()
dilimle3 = df1.loc["g":, "A": "C"]
print(dilimle3)
print()
dilimle4 = df1.loc[:"d", "D":]
print(dilimle4)
print("_"*200)

df2 = pd.DataFrame(data=np.random.randint(1, 20, size=(5, 3)),
                   index=list("abcde"),
                   columns=list("ABC"))

print(df2)
print()
print(df2.loc["b"] < 15)
print()
print(df2.loc["c"] > 10)
print()
print(df2.loc["e"] == 12)
print()
print(df2.loc["a"] != 14)
print("_"*200)

seri1 = pd.Series(data=list("abcxyzprs"),
                  index=[3, 6, 2, 1, 4, 0, 5, 7, 8])

print(seri1)
print()
print(seri1.loc[1:5])
print()
print(seri1.loc[:0])
print()
print(seri1.iloc[3:6])
print()
print(seri1.iloc[5:])
print()
print(seri1.sort_index(ascending=False))
print()
print(seri1.sort_index(ascending=True))
print()
print(seri1.sort_index().iloc[0:6])
print()
print(seri1.sort_index(ascending=False).loc[7:2])
print("_"*200)

seri2 = pd.Series(data=list([1, 2, 3, 4, 5, 6, 7, 8, 9]),
                  index=list("abcdefghj"))

print(seri2)
print()
print(seri2.sample()) # sample yöntemiyle bir seri yada dataframe den rastgele satır veya sütun seçeriz
print()
print(seri2.sample(n=3)) # n parametresi ile kaç adet rastgele satır veya sütun seçmek istediğimizi belirtiriz
print()
print(seri2.sample(n=6, replace=True)) # replace true dersek aynı satır veya sütundan 1 den fazla adet seçme olasılığı olur
print("_"*100)


df3 = pd.DataFrame(data=np.random.randint(1, 10, size=(8, 6)),
                   index=list("abcdefgh"),
                   columns=list("ABCDEF"))

print(df3)
print()
print(df3.sample(n=4, axis=1, replace=True))
print("_"*100)


seri3 = pd.Series(data=[1, 2, 3, 4], index=list("abcd"))

print(seri3)
print()
seri3["e"] = 5.0
print(seri3)
print()
seri3["f"] = "altı"
print(seri3)
print("_"*100)

df4 = pd.DataFrame(np.arange(100, 108).reshape(4, 2),
                   columns=["A", "B"])

print(df4)
print()
df4["C"] = df4["A"]
print(df4)
print()
df4["D"] = df4["B"]
print(df4)
print()
df4[["E", "F", "G", "H"]] = df4[["A", "B", "C", "D"]]
print(df4)
print("_"*100)

# sadece bir skaler değere erişmek için en hızlı yol,
# tüm veri yapılarında uygulanan at ve iat yöntemlerini kullanmaktır


df5 = pd.DataFrame(np.arange(500, 524).reshape(6, 4),
                   columns=["A", "B", "C", "D"])

print(df5)
print()
print(df5.iat[4, 2])
print()
print(df5.iat[5, 3])
print()
print(df5.at[3, "B"])
print()
print(df5.at[0, "C"])
print("_"*100)

seri4 = pd.Series(range(-5, 10), index=list("abcdefghkmnoprs"))
print(seri4)
print()
print(seri4[seri4 > 0])
print()
print(seri4[seri4 < 0])
print()
print(seri4[(seri4 < -2) | (seri4 > 5)])
print()
print(seri4[(seri4 > -3) & (seri4 > 2) & (seri4 > 6)])
print()
print(seri4[~(seri4 < 4)])
print()
print(seri4[~(seri4 > 0)])
print()
print(seri4[~(seri4 % 2 == 0)])
print()
print(seri4[~(seri4 % 3 == 0)])
print("_"*100)

seri5 = pd.Series(np.arange(100, 115),
                  index=list("abcdefghkmnoprs"))

print(seri5)
print()
print(seri5.isin([102, 104, 105, 107, 108, 110, 111, 113]))
print()
print(seri5.index.isin(["a", "d", "ğ", "i", "j", "k", "m", "n"]))
print()
print(seri5.index.isin(["g", "h", "k", "m", "n", "o", "p", "r", "s"]))
print()
print(seri5.isin([100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110]))
print("_"*100)

df6 = pd.DataFrame({"değerler": [100, 200, 300, 400, 300, 200],
                    "id1": ["a", "b", "c", "d", "e", "f"],
                    "id2": ["g", "c", "j", "b", "a", "d"]})

print(df6)
print()
search = [100, 400, 500, "b", "e", "f", "g", "j", "k", "m"]
print(df6.isin(search))
print()
print(df6.isin([200, 400, "a", "c", "f", "j", "b", "d"]))
print("_"*100)

df7 = pd.DataFrame(np.random.randint(100, 110, size=(10, 4)),
                   columns=list("abcd"))
print(df7)
print()
print(df7[(df7["a"] < df7["b"]) & (df7["c"] > df7["d"])])
print()
print(df7[(df7["a"] > df7["b"]) & (df7["c"] > df7["d"])])
print()
print(df7[(df7["a"] < df7["b"]) & (df7["c"] < df7["d"])])
print()
print(df7.query("(a > b) & (c > d)"))
print()
print(df7.query("(a < b) & (c < d)"))
print()
print(df7.query("(a < b) | (c > d)"))
print()
print(df7.query("(a == b) | (c < d)"))
print()
print(df7.query("(a == b) & (c > d)"))
print("_"*100)

df8 = pd.DataFrame(np.random.randint(1, 10, size=(10, 4)),
                   columns=list("abcd"))

print(df8)
print()
print(df8.query("index < a < b"))
print()
print(df8.query("index > c == d"))
print()
print(df8.query("index == b == c"))
print()
print(df8.query("index > a > b > c > d"))
print()
print(df8.query("a > 5"))
print()
print(df8.query("b == 7"))
print()
print(df8.query("c < 4"))
print()
print(df8.query("d != 3"))
print("_"*100)
df8.index.name = "x"
print(df8)
print()
print(df8.query("x > a > d"))
print()
print(df8.query("x < b > c"))
print()
print(df8.query("x == c == a"))
print()
print(df8.query("(x > b) & (x < d)"))
print()
print(df8.query("(x == c) | (x < a)"))
print("_"*100)

df9 = pd.DataFrame({"x": list("aabbccddeeff"), "y": list("aaaabbbbcccc"),
                    "c": np.random.randint(0, 5, size=12),
                    "d": np.random.randint(0, 10, size=12)})

print(df9)
print()
print(df9.query("x in y"))
print()
print(df9.query("x not in y"))
print()
print(df9.query("c in d"))
print()
print(df9.query("c not in d"))
print()
print(df9.query("d in c"))
print()
print(df9.query("d not in c"))
print("_"*100)

df10 = pd.DataFrame(np.random.randint(5, 10, size=(10, 4)),
                    columns=list("abcd"))

print(df10)
print()
sorgu1 = df10.query("(a > b > c) and (((a + d) > (c + b)) or (a * b) > 80)")
print(sorgu1)
print()
sorgu2 = df10.query("(a < b) and (((a * c) > (b * d)) and (a + b + c + d) < 30)")
print(sorgu2)
print()
sorgu3 = df10.query("(a ** 2 > 80) and (((c ** 2) > (b ** 3)) or (a * b * c * d) > 5000)")
print(sorgu3)
print("_"*100)


renkler = np.random.choice(["beyaz", "mavi", "yeşil"], size=10)
yiyecekler = np.random.choice(["peynir", "zeytin", "ekmek"], size=10)
print(renkler)
print(yiyecekler)
print("_"*50)

indeks = pd.MultiIndex.from_arrays([renkler, yiyecekler],
                                  names=["renk", "yiyecek"])

df11 = pd.DataFrame(np.random.randint(10, 20, size=(10, 2)), index=indeks)
print(df11)
print()
print(indeks.get_level_values(0))
print()
print(indeks.get_level_values(1))
print("_"*100)

df12 = pd.DataFrame(np.random.randint(1, 10, size=(3, 10)),
                    index=["A", "B", "C"], columns=indeks)

print(df12)
print()
#print(df12["beyaz"])

#print(df12["mavi"])

#print(df12["yeşil"])

#print(df12["beyaz", "peynir"])

#print(df12["mavi", "zeytin"])

#print(df12["yeşil", "ekmek"])

#print(df12["yeşil"]["ekmek"])

#print(df12["mavi"]["zeytin"])

#print(df12[["mavi", "beyaz"]])

#print(df12[["yeşil", "beyaz"]])

#print(df12[["mavi", "yeşil"]])

print(df12.columns)
print()
print(df12.index)
print()
print(df12.columns.levels)
print("_"*100)

colors = np.random.choice(["eflatun", "turuncu", "mor"], size=10)
foods = np.random.choice(["et", "tavuk", "balık"], size=10)
arrays = [colors, foods]

seri5 = pd.Series(np.random.randint(10, 20, size=(10)), index=arrays)
print(seri5)
print()
#print(seri5[2:5])
#print(seri5[4:8])
#print(seri5[4:8][3])
#print(seri5[3:5])
#print(seri5[3:5][0])
#print(seri5[1:8])
#print(seri5[1:8][4])
print(seri5.index)
print("_"*100)

#print(df12.T)
#print()

renkler = np.random.choice(["pembe", "sarı", "turkuaz"], size=10)
yiyecekler = np.random.choice(["pizza", "makarna", "hamburger"], size=10)
print(renkler)
print(yiyecekler)
print("_"*50)

indeks = pd.MultiIndex.from_arrays([renkler, yiyecekler],
                                  names=["renk", "yiyecek"])

df13 = pd.DataFrame(np.random.randint(10, 20, size=(10, 3)),
                    index=indeks, columns=["X", "Y", "Z"])
print(df13)
print()
#print(df13.loc[("turkuaz", "hamburger")])
#print(df13.loc[("sarı", "pizza")])
#print(df13.loc[("pembe", "makarna")])
#print(df13.loc[("turkuaz", "pizza"), "Z"])
#print(df13.loc[("sarı", "makarna"), "X"])
#print(df13.loc[("pembe", "hamburger"), "Y"])
#print(df13.loc[("sarı", "makarna"), ("X", "Y")])
#print(df13.loc[("turkuaz", "pizza"), ("Y", "Z")])
#print(df13.loc[("pembe", "hamburger"), ("Z", "Y", "X")])
#print(df13.loc["sarı"])
#print()
#print(df13.loc["turkuaz"])
#print()
#print(df13.loc["pembe"])
#print(df13.loc["sarı", ("X")])
#print(df13.loc["turkuaz", ("X", "Z")])
#print(df13.loc["pembe", ("X", "Y", "Z")])

#print(df13.iloc[2:5])
#print(df13.iloc[4:8]["X"])
#print(df13.iloc[3:6][["X", "Y", "Z"]])
#print(df13.iloc[0:3][["Y", "Z"]])
#print(df13.iloc[0:4, 1:3])
#print(df13.iloc[2:6, 0:1])
#print(df13.iloc[1:5, :])
#print(df13.iloc[0:1, 0:1])

#print(df13.query('renk == "turkuaz"'))
#print(df13.query('yiyecek == "makarna"'))
#print(df13.query('renk != "sarı"'))
#print(df13.query('yiyecek != "hamburger"'))

#print(df13.query("((renk == 'turkuaz') & (yiyecek == 'hamburger'))"))
#print(df13.query("((renk == 'sarı') & (yiyecek == 'pizza'))"))
#print(df13.query("((renk == 'pembe') & (yiyecek == 'makarna'))"))

#print(df13.query("((renk == 'sarı') | (yiyecek == 'hamburger'))"))
#print(df13.query("((renk == 'turkuaz') | (yiyecek == 'pizza'))"))
#print(df13.query("((renk == 'pembe') | (yiyecek == 'makarna'))"))




































