import pandas as pd

veri = pd.Series([0.15, 0.25, 0.35, 0.45, 0.55, 0.65, 0.75])
print(veri)
print()
print(veri.values)
print()
print(veri.index)
print()
print(veri[5])
print()
print(veri[0])
print()
print(veri[0:4])
print()
print(veri[2:5])
print("_"*200)

veri2 = pd.Series(data=["x", "y", "z","a","b","c"],
                  index=[12, 14, 18, 23, 25, 27])

print(veri2)
print()
print(veri2[0:3])
print()
print(veri2.loc[12:25])
print()
print(veri2.iloc[1:5])
print()
print(veri2.loc[18:25])
print()
print(veri2.iloc[3:6])
print()
print("_"*200)

nüfus = pd.Series({"Balıkesir": 2500000, "Edirne": 1200000,
                   "Malatya": 750000, "Antalya": 1500000,
                   "Gaziantep": 600000, "Sakarya": 900000})

alan = pd.Series({"Balıkesir": 2624, "Edirne": 3278,
                  "Malatya": 4106, "Antalya": 5851,
                  "Gaziantep": 1873, "Sakarya": 1497})

veri3 = pd.DataFrame({"alan": alan, "nüfus": nüfus})
print(veri3)
print()
print(veri3["alan"])
print()
print(veri3["nüfus"])
print()
veri3["yoğunluk"] = veri3["nüfus"] / veri3["alan"]
print(veri3)
print()
print(veri3.yoğunluk)
print()
print(veri3.nüfus)
print()
print(veri3.alan)
print()
#print(veri3.T.to_string())
print()
print(veri3.values)
print()
print(veri3.values[0])
print()
print(veri3["alan"][0])
print(veri3["nüfus"][4])
print(veri3["yoğunluk"][3])
print()
print(veri3.iloc[1:4, 0:2])
print()
print(veri3.iloc[3:5, 1:3])
print()
print(veri3.loc["Balıkesir": "Antalya", :])
print()
print(veri3.loc["Malatya": "Sakarya", "nüfus"])
print()
print(veri3.loc["Edirne": "Antalya", "alan": "nüfus"])
print()
print(veri3.loc[veri3.yoğunluk < 500, ["alan", "nüfus"]])
print()
print(veri3.loc[veri3.alan > 3000, ["yoğunluk"]])
print()
print(veri3.loc[veri3.nüfus != 900000, ["alan"]])
print()
veri3.iloc[2, 0] = 7835
print(veri3)
print()
veri3.iloc[4, 1] = 400000
print(veri3)
veri3.iloc[-1, 2] = 701
print(veri3)
print()
print(veri3[veri3.yoğunluk < 500])
print()
print(veri3[veri3.nüfus > 1000000])



