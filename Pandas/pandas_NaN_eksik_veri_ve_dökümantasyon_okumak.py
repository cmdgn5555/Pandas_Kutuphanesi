
import pandas as pd
import numpy as np

#ögrenciler = {"İlhan": pd.Series(data=[21, "akyol", "edebiyat", 173],
#                                 index=["yaş", "soyisim", "bölüm", "boy"]),
#              "Saliha": pd.Series(data=[20, "bayan", "matematik", 65],
#                                 index=["yaş", "cinsiyet", "bölüm", "kilo"]),
#              "Murat": pd.Series(data=[18, "eroğlu", "felsefe", 178],
#                                 index=["yaş", "soyisim", "bölüm", "boy"])}
#
#df_ögrenciler = pd.DataFrame(ögrenciler)
#print(df_ögrenciler)
#print("_"*50)
#
#a = df_ögrenciler.isnull()
#print(a)
#print(type(a))
#print("_"*50)
#
#b = df_ögrenciler.isnull().sum()
#print(b)
#print(type(b))
#print("_"*50)
#
#c = df_ögrenciler.isnull().sum().sum()
#print(c)
#print(type(c))


#ögrenciler = {"İlhan": pd.Series(data=[21, "akyol", "edebiyat", 173],
#                                 index=["yaş", "soyisim", "bölüm", "boy"]),
#              "Saliha": pd.Series(data=[20, "bayan", "matematik", 65],
#                                 index=["yaş", "cinsiyet", "bölüm", "kilo"]),
#              "Murat": pd.Series(data=[18, "eroğlu", "felsefe", 178],
#                                 index=["yaş", "soyisim", "bölüm", "boy"])}
#
#df_ögrenciler = pd.DataFrame(ögrenciler)
#print(df_ögrenciler)
#print("_"*50)
#
#a = df_ögrenciler.notnull()
#print(a)
#print(type(a))
#print("_"*50)
#
#b = df_ögrenciler.notnull().sum()
#print(b)
#print(type(b))
#print("_"*50)
#
#c = df_ögrenciler.notnull().sum().sum()
#print(c)
#print(type(c))

#ögrenciler = {"İlhan": pd.Series(data=[21, "akyol", "edebiyat", 173],
#                                 index=["yaş", "soyisim", "bölüm", "boy"]),
#              "Saliha": pd.Series(data=[20, "bayan", "matematik", 65],
#                                 index=["yaş", "cinsiyet", "bölüm", "kilo"]),
#              "Murat": pd.Series(data=[18, "eroğlu", "felsefe", 178],
#                                 index=["yaş", "soyisim", "bölüm", "boy"])}
#
#df_ögrenciler = pd.DataFrame(ögrenciler)
#print(df_ögrenciler)
#print("_"*50)
#
#a = df_ögrenciler.count()
#print(a)
#print(type(a))
#print("_"*50)
#
#b = df_ögrenciler.count().sum()
#print(b)
#print(type(b))
#print("_"*50)

#ögrenciler = {"İlhan": pd.Series(data=[21, "akyol", "edebiyat", 173],
#                                 index=["yaş", "soyisim", "bölüm", "boy"]),
#              "Saliha": pd.Series(data=[20, "bayan", "matematik", 65],
#                                 index=["yaş", "cinsiyet", "bölüm", "kilo"]),
#              "Murat": pd.Series(data=[18, "eroğlu", "felsefe", 178],
#                                 index=["yaş", "soyisim", "bölüm", "boy"])}
#
#df_ögrenciler = pd.DataFrame(ögrenciler)


#df_ögrenciler.dropna(inplace=True, axis=1)
#print(df_ögrenciler)
#print(type(df_ögrenciler))
#print("_"*50)
#
#df_ögrenciler.dropna(inplace=True, axis=0)
#print(df_ögrenciler)
#print(type(df_ögrenciler))

#df_ögrenciler["Saliha"]["kilo"] = None
#df_ögrenciler["Saliha"]["cinsiyet"] = None
#df_ögrenciler["İlhan"]["boy"] = None
#df_ögrenciler["Murat"]["boy"] = None
#df_ögrenciler["Saliha"]["yaş"] = None
#df_ögrenciler["İlhan"]["yaş"] = None
#df_ögrenciler["Murat"]["yaş"] = None
#df_ögrenciler["Saliha"]["bölüm"] = None
#df_ögrenciler["İlhan"]["bölüm"] = None
#df_ögrenciler["Murat"]["bölüm"] = None
#df_ögrenciler["İlhan"]["soyisim"] = None
#df_ögrenciler["Murat"]["soyisim"] = None

#print(df_ögrenciler)
#print("_"*50)
#
#df_ögrenciler.dropna(how="all", inplace=True)
#print(df_ögrenciler)
#print(type(df_ögrenciler))
#print("_"*50)

#print(df_ögrenciler)
#print("_"*50)

#df_ögrenciler.dropna(how="any", inplace=True)
#print(df_ögrenciler)
#print(type(df_ögrenciler))

#print(df_ögrenciler)
#print("_"*50)

#df_ögrenciler.dropna(thresh=5, inplace=True, axis=1)
#print(df_ögrenciler)
#print(type(df_ögrenciler))

#df_ögrenciler.dropna(thresh=4, inplace=True, axis=0)
#print(df_ögrenciler)
#print(type(df_ögrenciler))

#df_ögrenciler.fillna(method="ffill", axis=0, inplace=True)
#print(df_ögrenciler)
#print("_"*50)

#df_ögrenciler.fillna(method="ffill", axis=1, inplace=True)
#print(df_ögrenciler)

#df_ögrenciler.fillna(method="bfill", axis=0, inplace=True)
#print(df_ögrenciler)

#df_ögrenciler.fillna(method="bfill", axis=1, inplace=True)
#print(df_ögrenciler)

data = pd.Series([10, 20, np.nan, "java", "python", None])
print(data)
print(data.isnull())
print()
print(data[data.notnull()])
print()
print(data[data.isnull()])
print()
print(data.notnull())
print()
data.dropna(inplace=True)
print(data)
print("_"*200)

df = pd.DataFrame([[5, np.nan, 3],
                   [2, 14, 20],
                   [np.nan, 44, 16]])

print(df)
print()
print(df.dropna(axis=0))
print()
print(df.dropna(axis=1))
print()
df["bos_degerler"] = np.nan
print(df)
print()
#print(df.dropna(axis=1, how="all", inplace=True))
#print(df)
#print(df.dropna(axis=0, how="any", inplace=True))
#print(df)
print()
df.iloc[2, 3] = 77
print(df)
print()
#print(df.dropna(axis=1, inplace=True, thresh=3))
#print(df)
print(df.dropna(axis=0, inplace=True, thresh=3))
print(df)
print("_"*200)

veri = pd.Series([3, np.nan, 8, None, 7, pd.NA, 16, np.nan, None, 22], index=list("abcdefghjk"))
print(veri)
print()
veri.fillna("python", inplace=True)
print(veri)

#veri.fillna(method="ffill", inplace=True)
#print(veri)

#veri.fillna(method="bfill", inplace=True)
#print(veri)

#veri2 = pd.DataFrame([[9, 8, 8, None, 93, pd.NA, 45],
#                   [14, 24, None, pd.NA, 23, 106, 11],
#                   [np.nan, pd.NA, 20, 12, None, None, 33],
#                   [26, 10, np.nan, None, 30, 102, pd.NA],
#                   [26, 10, np.nan, None, 30, 102, pd.NA],
#                   [26, 10, np.nan, None, 30, 102, pd.NA],
#                   [26, 10, np.nan, None, 30, 102, pd.NA]])
#
#print(veri2)
#print()

#veri2.fillna("doldur", inplace=True)
#print(veri2)

#veri2.fillna(method="ffill", inplace=True, axis=0)
#print(veri2)

#veri2.fillna(method="ffill", inplace=True, axis=0)
#print(veri2)

#veri2.fillna(method="bfill", inplace=True, axis=1)
#print(veri2)
print("_"*200)

ögrenciler = {"İlhan": pd.Series(data=[21, "akyol", "edebiyat", 173],
                                 index=["yaş", "soyisim", "bölüm", "boy"]),
              "Saliha": pd.Series(data=[20, "bayan", "matematik", 65],
                                 index=["yaş", "cinsiyet", "bölüm", "kilo"]),
              "Murat": pd.Series(data=[18, "eroğlu", "felsefe", 178],
                                 index=["yaş", "soyisim", "bölüm", "boy"])}

df_ögrenciler = pd.DataFrame(ögrenciler)
print(df_ögrenciler)
print()
#df_ögrenciler.fillna(inplace=True, axis=1, method="ffill")
#print(df_ögrenciler)

#df_ögrenciler.fillna(inplace=True, axis=1, method="bfill")
#print(df_ögrenciler)












