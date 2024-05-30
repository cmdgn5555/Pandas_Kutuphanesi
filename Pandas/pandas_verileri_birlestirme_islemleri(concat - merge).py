
from IPython.display import Image
import pandas as pd
from pprint import pprint

#CONCAT

df1 = pd.DataFrame({"A": ["A0", "A1", "A2", "A3"],
                    "B": ["B0", "B1", "B2", "B3"],
                    "C": ["C0", "C1", "C2", "C3"],
                    "D": ["D0", "D1", "D2", "D3"]},
                   index=[0, 1, 2, 3])

print(df1)
print()

df2 = pd.DataFrame({"A": ["A4", "A5", "A6", "A7"],
                    "B": ["B4", "B5", "B6", "B7"],
                    "C": ["C4", "C5", "C6", "C7"],
                    "D": ["D4", "D5", "D6", "D7"]},
                   index=[4, 5, 6, 7])

print(df2)
print()

df3 = pd.DataFrame({"A": ["A8", "A9", "A10", "A11"],
                    "B": ["B8", "B9", "B10", "B11"],
                    "C": ["C8", "C9", "C10", "C11"],
                    "D": ["D8", "D9", "D10", "D11"]},
                   index=[8, 9, 10, 11])

print(df3)
print()

liste = [df1, df2, df3]
pprint(liste)
print("_"*100)

result = pd.concat(liste, axis=0)
print(df1, "\n", df2, "\n", df3)
print(result)
print("_"*100)

result2 = pd.concat(liste, axis=1)
print(df1, "\n", df2, "\n", df3)
print(result2)
print("_"*200)


df4 = pd.DataFrame({"A": ["A0", "A1", "A2", "A3"],
                    "B": ["B0", "B1", "B2", "B3"],
                    "C": ["C0", "C1", "C2", "C3"],
                    "D": ["D0", "D1", "D2", "D3"]},
                   index=[0, 1, 2, 5])

print(df4)
print()

df5 = pd.DataFrame({"A": ["A4", "A5", "A6", "A7"],
                    "B": ["B4", "B5", "B6", "B7"],
                    "C": ["C4", "C5", "C6", "C7"],
                    "D": ["D4", "D5", "D6", "D7"]},
                   index=[0, 1, 7, 3])

print(df5)
print()

df6 = pd.DataFrame({"A": ["A8", "A9", "A10", "A11"],
                    "B": ["B8", "B9", "B10", "B11"],
                    "C": ["C8", "C9", "C10", "C11"],
                    "D": ["D8", "D9", "D10", "D11"]},
                   index=[0, 1, 8, 3])

print(df5)
print("\n")

liste2 = [df4, df5, df6]

result3 = pd.concat(liste2, axis=0, ignore_index=True)
print(df4, "\n", df5, "\n", df6)
print(result3)
print("_"*200)

# keys parametresi girilecekse ignore_index parametresi false olmalıdır

result4 = pd.concat(liste2, keys=["df4", "df5", "df6"],
                    ignore_index=False)

print(result4)
print()

print(result4.loc["df4"])
print()
print(result4.loc["df6"])
print()
print(result4.loc["df5", 7])
print()
print(result4.loc["df4", 2])
print()
print(result4.index.get_level_values(0))
print()
print(result4.index.get_level_values(1))
print()
print(result4.index.levels)
print("_"*100)

seri1 = pd.Series(["X0", "X1", "X2", "X3"], name="X")
print(seri1)
print()
print(df4)
print()
result5 = pd.concat([df4, seri1], axis=1, ignore_index=False)
print(result5)
print("_"*100)
result6 = pd.concat([df4, seri1], axis=1, ignore_index=True)
print(result6)
print("_"*100)
result7 = pd.concat([df4, seri1], axis=0, ignore_index=False)
print(result7)
print("_"*100)
result8 = pd.concat([df4, seri1], axis=0, ignore_index=True)
print(result8)
print("_"*100)
seri2 = pd.Series(["0", "1", "2", "3"])
result9 = pd.concat([df4, seri2, seri2, seri1, seri1],
                    axis=1, ignore_index=True)
print(seri2)
print()
print(df4)
print()
print(result9)
print("_"*100)

result10 = pd.concat([df4, seri2, seri2, seri1, seri1],
                    axis=0, ignore_index=True)
print(seri2)
print()
print(df4)
print()
print(result10)
print("_"*100)

seri3 = pd.Series([0, 1, 2, 3])
seri4 = pd.Series([0, 1, 2, 3])
seri5 = pd.Series([0, 1, 4, 5])

result11 = pd.concat([seri3, seri4, seri5], axis=1)
print(result11)
print()
result12 = pd.concat([seri3, seri4, seri5], axis=0)
print(result12)
print()
result13 = pd.concat([seri3, seri4, seri5], axis=1,
                     keys=["mavi", "sarı", "pembe"])
print(result13)
print()
result14 = pd.concat([seri3, seri4, seri5], axis=0,
                     keys=["mavi", "sarı", "pembe"])
print(result14)




# MERGE

print("_"*500)

sol = pd.DataFrame({
    "key": ["K0", "K1", "K2", "K3"],
    "A": ["AO", "A1", "A2", "A3"],
    "B": ["B0", "B1", "B2", "B3"]})

sag = pd.DataFrame({
    "key": ["K0", "K1", "K2", "K3"],
    "C": ["C0", "C1", "C2", "C3"],
    "D": ["D0", "D1", "D2", "D3"]})

print(sol)
print()
print(sag)
print()
sonuc1 = pd.merge(sol, sag, on="key")
print(sonuc1)
print("_"*100)

su_elektrik = pd.read_csv("su_elektrik.csv", sep=";")
dogalgaz = pd.read_csv("dogalgaz.csv", sep=";")

print(su_elektrik.head().to_string())
print()
print(dogalgaz.head().to_string())
print("_"*100)
print(su_elektrik.to_string())
print()
print(dogalgaz.to_string())
print()

inner_join = pd.merge(left=su_elektrik,
                      right=dogalgaz,
                      left_on="KULLANICI_ID",
                      right_on="KULLANICI_ID",
                      how="inner")

print(inner_join.to_string())
print()
print(su_elektrik.shape)
print(dogalgaz.shape)
print(inner_join.shape)
print()
inner_join2 = pd.merge(left=dogalgaz,
                       right=su_elektrik,
                       on="SOYAD",
                       how="inner")
print(inner_join2.to_string())
print("_"*100)

inner_join3 = pd.merge(left=dogalgaz,
                       right=su_elektrik,
                       on="KULLANICI_ID",
                       how="inner",
                       suffixes=("_dogal", "_su_elk"))

print(inner_join3.to_string())
print("_"*100)

print(su_elektrik["KULLANICI_ID"].isin(dogalgaz["KULLANICI_ID"]))
print()
print(su_elektrik["ŞEHİR"].isin(dogalgaz["ŞEHİR"]))
print()
print(su_elektrik["KULLANICI_ID"].isin(dogalgaz["KULLANICI_ID"]).value_counts())
print()
print(su_elektrik["ŞEHİR"].isin(dogalgaz["ŞEHİR"]).value_counts())
print("_"*100)

print(su_elektrik.columns)
print()
print(dogalgaz.columns)
print("\n")

su_elektrik.rename(columns={"KULLANICI_ID": "USER_ID"},
                   inplace=True)

print(su_elektrik.to_string())
print("\n")

dogalgaz.rename(columns={"ŞEHİR": "CİTY"},
                inplace=True)

print(dogalgaz.to_string())
print("_"*100)

inner_join4 = pd.merge(left=su_elektrik,
                       right=dogalgaz,
                       left_on="USER_ID",
                       right_on="KULLANICI_ID",
                       how="inner")

print(inner_join4.to_string())
print()
print(inner_join4.shape)
print("_"*100)

inner_join5 = pd.merge(left=dogalgaz,
                       right=su_elektrik,
                       left_on="CİTY",
                       right_on="ŞEHİR",
                       how="inner")

print(inner_join5.to_string())
print()
print(inner_join4.shape)
print("_"*100)

inner_join6 = pd.merge(left=su_elektrik,
                       right=dogalgaz,
                       left_on=["AD", "SOYAD"],
                       right_on=["AD", "SOYAD"],
                       how="inner")

print(inner_join6.to_string())
print("_"*100)

inner_join7 = pd.merge(left=su_elektrik,
                       right=dogalgaz,
                       left_on=["USER_ID", "ŞEHİR"],
                       right_on=["KULLANICI_ID", "CİTY"],
                       indicator=True,
                       how="inner")

print(inner_join7.to_string())
print()

print(inner_join7["AD_x"].value_counts())
print()
print(inner_join7[["USER_ID", "KULLANICI_ID"]].value_counts())
print()
print(inner_join7["CİTY"].value_counts())
print()
print(inner_join7["ŞEHİR"].value_counts())
print()
print(inner_join7["_merge"].value_counts())
print("_"*200)

su_elektrik.rename(columns={"USER_ID": "KULLANICI_ID"},
                   inplace=True)

dogalgaz.rename(columns={"CİTY": "ŞEHİR"},
                inplace=True)

print(su_elektrik.to_string())
print()
print(dogalgaz.to_string())
print("\n\n")

left_join = pd.merge(left=su_elektrik,
                     right=dogalgaz,
                     on="KULLANICI_ID",
                     indicator=True,
                     how="left")

print(left_join.to_string())
print("\n")
print(left_join.shape)
print(left_join["_merge"].value_counts())
print("\n\n")

left_join2 = pd.merge(left=dogalgaz,
                     right=su_elektrik,
                     on="KULLANICI_ID",
                     indicator=True,
                     how="left")

print(left_join2.to_string())
print(left_join2["_merge"].value_counts())
print("_"*200)

right_join = pd.merge(left=su_elektrik,
                      right=dogalgaz,
                      on="KULLANICI_ID",
                      indicator=True,
                      how="right")

print(right_join.to_string())
print(right_join["_merge"].value_counts())
print("\n\n\n")

right_join2 = pd.merge(left=dogalgaz,
                      right=su_elektrik,
                      on="AD",
                      indicator=True,
                      how="right")

print(right_join2.to_string())
print(right_join2["_merge"].value_counts())
print("_"*200)

full_outer_join = pd.merge(left=su_elektrik,
                           right=dogalgaz,
                           on="KULLANICI_ID",
                           indicator=True,
                           how="outer")

print(full_outer_join.to_string())
print(full_outer_join["_merge"].value_counts())
print("_"*200)

data1 = pd.DataFrame({"str": ["A", "B"]})
data2 = pd.DataFrame({"int": [1, 2]})

print(data1)
print(data2)
print("\n")

cross_join1 = pd.merge(left=data1, right=data2, how="cross")
print(cross_join1)
print()
cross_join2 = pd.merge(left=data2, right=data1, how="cross")
print(cross_join2)
print("_"*200)

cross_join3 = pd.merge(left=su_elektrik,
                       right=dogalgaz,
                       indicator=True,
                       how="cross",
                       )

print(cross_join3.head(50).to_string())
print("_"*200)

veri1 = pd.DataFrame({"ülkeler": ["fransa", "almanya", "hollanda"]})
veri2 = pd.DataFrame({"şehirler": ["paris", "berlin", "amsterdam"]})

print(veri1)
print()
print(veri2)
print()
cross_join4 = pd.merge(left=veri1,
                       right=veri2,
                       indicator=True,
                       how="cross")

print(cross_join4.to_string())
print()

cross_join5 = pd.merge(left=veri2,
                       right=veri1,
                       indicator=True,
                       how="cross")

print(cross_join5.to_string())
print(cross_join5["_merge"].value_counts())
print("_"*300)

dataframe1 = pd.DataFrame({
    "A": ["A0", "A1", "A2", "A3"],
    "B": ["B0", "B1", "B2", "B3"],
    "C": ["C0", "C1", "C2", "C3"],
    "D": ["D0", "D1", "D2", "D3"]},
    index=[0, 1, 2, 3])

dataframe2 = pd.DataFrame({
    "B": ["B2", "B3", "B6", "B7"],
    "D": ["D2", "D3", "D6", "D7"],
    "F": ["F2", "F3", "F6", "F7"],
    },
    index=[2, 3, 6, 7])

print(dataframe1)
print()
print(dataframe2)
print("\n\n")

sonuc2 = pd.concat([dataframe1, dataframe2],
                   axis=1,
                   join="inner")

print(sonuc2)
print("\n")

sonuc3 = pd.concat([dataframe1, dataframe2],
                   axis=0,
                   join="inner")

print(sonuc3)
print("\n")

sonuc4 = pd.concat([dataframe1, dataframe2],
                   axis=1,
                   join="outer")

print(sonuc4)

print("\n")

sonuc5 = pd.concat([dataframe1, dataframe2],
                   axis=0,
                   join="outer")

print(sonuc5)


























