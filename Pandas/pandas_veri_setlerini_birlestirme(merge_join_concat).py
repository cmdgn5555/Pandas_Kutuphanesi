
import pandas as pd
import numpy as np

# MERGE

v1 = pd.DataFrame({"anahtar": ["a", "b", "x", "c", "d", "e"],
                   "say1": range(30, 24, -1)})
v2 = pd.DataFrame({"anahtar": ["b", "c", "d", "e"],
                   "say2": range(25, 29)})

print(v1)
print()
print(v2)
print()
#print(pd.merge(v1, v2))
print(pd.merge(left=v2, right=v1, on="anahtar"))
print("_"*500)

v3 = pd.DataFrame({"anahtar1": ["y", "b", "x", "c", "d", "e"],
                   "say1": range(30, 24, -1)})
v4 = pd.DataFrame({"anahtar2": ["b", "c", "d", "e"],
                   "say2": range(25, 29)})

print(v3)
print()
print(v4)
print()
print(pd.merge(left=v3,
               right=v4,
               left_on="anahtar1",
               right_on="anahtar2",
               how="right"))
print("_"*500)


v5 = pd.DataFrame({"anahtar": ["a", "b", "x", "c", "d", "e"],
                   "say1": range(30, 24, -1),
                   "rakamlar": ["bir", "bir", "iki", "üç", "üç", "bir"]})
v6 = pd.DataFrame({"anahtar": ["b", "c", "d", "z"],
                   "say2": range(25, 29),
                   "rakamlar": ["bir", "üç", "üç", "bir"]})

print(v5)
print()
print(v6)
print()
print(pd.merge(left=v5, right=v6, on=["anahtar", "rakamlar"], how="inner"))
print()
print(pd.merge(left=v5, right=v6, on=["anahtar", "rakamlar"], how="outer"))
print()
print(pd.merge(left=v5,
               right=v6,
               on="anahtar",
               how="outer",
               suffixes=["_veri5", "_veri6"]))
print()
print(pd.merge(left=v5,
               right=v6,
               on="anahtar",
               how="inner",
               suffixes=[" veri5", " veri6"]))

print("_"*500)


df1 = pd.DataFrame({"harf": ["x", "x", "y", "y", "x", "z"],
                    "say": range(10, 16)})

print(df1)
print()

df2 = pd.DataFrame({"deger": [3, 5, 7]}, index=["x", "y", "h"])
print(df2)
print()
print(pd.merge(left=df1,
               right=df2,
               left_on="harf",
               right_index=True,
               how="outer"))
print()

print(pd.merge(left=df1,
               right=df2,
               left_on="harf",
               right_index=True,
               how="inner"))
print("_"*500)



dataframe1 = pd.DataFrame(data=[[5, 10], [15, 20], [25, 30]],
                          index=["x", "y", "z"],
                          columns=["fatih", "hasan"])
print(dataframe1)
print()

dataframe2 = pd.DataFrame(data=[[9, 19], [29, 39], [49, 59], [69, 79]],
                          index=["x", "a", "b", "c"],
                          columns=["tuna", "suna"])
print(dataframe2)
print()

print(pd.merge(left=dataframe1,
         right=dataframe2,
         right_index=True,
         left_index=True,
         how="outer"))

print()

print(pd.merge(left=dataframe1,
         right=dataframe2,
         right_index=True,
         left_index=True,
         how="inner"))

print("_"*500)

#JOİN

dataframe3 = pd.DataFrame(data=[[101, 102], [103, 104], [105, 106]],
                          index=["x", "y", "z"],
                          columns=["fatih", "hasan"])
print(dataframe3)
print()

dataframe4 = pd.DataFrame(data=[[200, 300], [400, 500], [600, 700], [800, 900]],
                          index=["x", "z", "b", "c"],
                          columns=["tuna", "suna"])
print(dataframe4)
print()
print(dataframe3.join(dataframe4, how="inner"))
print()
print(dataframe4.join(dataframe3, how="outer"))
print()

dataframe5 = pd.DataFrame(data=[[1500, 2500], [3500, 4500], [5500, 6500], [7500, 8500]],
                          index=["x", "y", "c", "z"],
                          columns=["merve", "engin"])

print(dataframe5)
print()
print(dataframe5.join([dataframe4, dataframe3], how="inner"))
print()
print(dataframe5.join([dataframe4, dataframe3], how="outer"))
print()
print(dataframe3.join([dataframe4, dataframe5], how="inner"))
print("_"*500)

#CONCAT

dizi = np.arange(100, 120).reshape(4, 5)
print(dizi)
print()
print(np.concatenate([dizi, dizi], axis=0))
print()
print(np.concatenate([dizi, dizi], axis=1))
print("_"*300)

veri1 = pd.Series(data=[13, 14], index=["a", "b"])
print(veri1)
print()
veri2 = pd.Series(data=[25, 26, 27], index=["c", "d", "e"])
print(veri2)
print()
veri3 = pd.Series(data=[32, 33], index=["f", "g"])
print(veri3)
print()
print(pd.concat([veri1, veri2, veri3], axis=0))
print()
print(pd.concat([veri1, veri2, veri3], axis=1))
print()
print(pd.concat([veri1, veri2, veri3], axis=1, join="inner"))
print()

veri4 = pd.Series(data=[310, 311, 312], index=["a", "b", "c"])
print(veri4)
print()

print(pd.concat([veri1, veri4],
                axis=1, join="inner"))
print()

print(pd.concat([veri1, veri4],
                axis=1, join="outer"))

print()

birlestir = pd.concat([veri1, veri2, veri3],
                      axis=1,
                      keys=["bir", "iki", "üç"])

print(birlestir)
print("_"*500)

vs1 = pd.DataFrame(data=np.arange(6).reshape(3, 2),
                   index=["a", "b", "c"],
                   columns=["bir", "iki"])
print(vs1)
print()

vs2 = pd.DataFrame(data=np.arange(10, 14).reshape(2, 2),
                   index=["a", "c"],
                   columns=["üç", "dört"])
print(vs2)
print()

birlestir2 = pd.concat([vs1, vs2], axis=1,
                       keys=["s1", "s2"])
print(birlestir2)
print("_"*500)

df3 = pd.DataFrame(data=np.random.randn(3, 4),
                   columns=["a", "b", "c", "d"])
print(df3)
print()

df4 = pd.DataFrame(np.random.randn(2, 3), columns=["a", "b", "c"])
print(df4)
print()

birlestir3 = pd.concat([df3, df4], axis=0, ignore_index=True)
print(birlestir3)
print()

birlestir4 = pd.concat([df3, df4], axis=1, ignore_index=False, keys=["sütun_1", "sütun_2"])
print(birlestir4)
print()

birlestir5 = pd.concat([df3, df4], axis=0, ignore_index=False, keys=["st1", "st2"])
print(birlestir5)
print()











