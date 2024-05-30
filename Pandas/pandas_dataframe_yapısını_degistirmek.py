import pandas as pd

#ögretmenler = {"Tolga": pd.Series(data=[40, "erkek", "tarih", 180], index=["yaş", "cinsiyet", "branş", "boy"]),
#               "Elif": pd.Series(data=[39, "kadın", "edebiyat", 165], index=["yaş", "cinsiyet", "branş", "boy"]),
#               "Rıza": pd.Series(data=[44, "erkek", "türkçe", 173], index=["yaş", "cinsiyet", "branş", "boy"])}

#df_ögretmenler = pd.DataFrame(ögretmenler)
#print(df_ögretmenler)
#print("_"*100)
#
#df_ögretmenler_2 = pd.DataFrame(ögretmenler, columns=["Tolga", "Rıza"])
#print(df_ögretmenler_2)
#print("_"*100)
#
#df_ögretmenler_3 = pd.DataFrame(ögretmenler, columns=["Elif"])
#print(df_ögretmenler_3)
#print("_"*100)
#
#df_ögretmenler_4 = pd.DataFrame(ögretmenler, index=["yaş"])
#print(df_ögretmenler_4)
#print("_"*100)
#
#df_ögretmenler_5 = pd.DataFrame(ögretmenler, index=["boy"])
#print(df_ögretmenler_5)
#print("_"*100)
#
#df_ögretmenler_6 = pd.DataFrame(ögretmenler, index=["cinsiyet", "branş"])
#print(df_ögretmenler_6)
#print("_"*100)
#
#df_ögretmenler_7 = pd.DataFrame(ögretmenler, columns=["Rıza", "Elif"],
#                                index=["branş", "boy"])
#print(df_ögretmenler_7)

#ögretmenler = {"Tolga": pd.Series(data=[40, "erkek", "tarih", 180],
#                                  index=["yaş", "cinsiyet", "branş", "boy"]),
#
#               "Elif": pd.Series(data=[39, "kadın", "edebiyat", 165],
#                                 index=["yaş", "cinsiyet", "branş", "boy"]),
#
#               "Rıza": pd.Series(data=[44, "erkek", "türkçe", 173],
#                                 index=["yaş", "cinsiyet", "branş", "boy"])}

#df_ögretmenler = pd.DataFrame(ögretmenler)
#print(df_ögretmenler)
#print()
#
#print(df_ögretmenler["Tolga"])
#print(type(df_ögretmenler["Tolga"]))
#print(df_ögretmenler["Tolga"].ndim)
#print("_"*50)
#
#print(df_ögretmenler[["Elif"]])
#print(type(df_ögretmenler[["Elif"]]))
#print(df_ögretmenler[["Elif"]].ndim)
#print("_"*50)
#
#print(df_ögretmenler[["Tolga", "Rıza"]])
#print(type(df_ögretmenler[["Tolga", "Rıza"]]))

#ögretmenler = {"Tolga": pd.Series(data=[40, "erkek", "tarih", 180],
#                                  index=["yaş", "cinsiyet", "branş", "boy"]),
#
#               "Elif": pd.Series(data=[39, "kadın", "edebiyat", 165],
#                                 index=["yaş", "cinsiyet", "branş", "boy"]),
#
#               "Rıza": pd.Series(data=[44, "erkek", "türkçe", 173],
#                                 index=["yaş", "cinsiyet", "branş", "boy"])}

#df_ögretmenler = pd.DataFrame(ögretmenler)
#print(df_ögretmenler)
#print()
#print("_"*50)
#
#print(df_ögretmenler.loc["yaş"])
#print(type(df_ögretmenler.loc["yaş"]))
#print("_"*50)
#
#print(df_ögretmenler.loc[["cinsiyet", "branş"]])
#print(type(df_ögretmenler.loc[["cinsiyet", "branş"]]))
#print("_"*50)
#
#print(df_ögretmenler.loc[["boy", "yaş", "branş"]])
#print(type(df_ögretmenler.loc[["boy", "yaş", "branş"]]))

#ögretmenler = {"Tolga": pd.Series(data=[40, "erkek", "tarih", 180],
#                                  index=["yaş", "cinsiyet", "branş", "boy"]),
#
#               "Elif": pd.Series(data=[39, "kadın", "edebiyat", 165],
#                                 index=["yaş", "cinsiyet", "branş", "boy"]),
#
#               "Rıza": pd.Series(data=[44, "erkek", "türkçe", 173],
#                                 index=["yaş", "cinsiyet", "branş", "boy"])}
#
#df_ögretmenler = pd.DataFrame(ögretmenler)
#print(df_ögretmenler)
#print("_"*50)

#print(df_ögretmenler["Tolga"]["branş"])
#print(df_ögretmenler["Elif"]["cinsiyet"])
#print(df_ögretmenler["Rıza"]["boy"])
#print("_"*100)
#
#print(df_ögretmenler["Tolga"][0])
#print(df_ögretmenler["Elif"][-1])
#print(df_ögretmenler["Rıza"][1])

#df_ögretmenler["Tolga"] = [50, "erkek", "fizik", 167]
#df_ögretmenler["Elif"] = [60, "kadın", "kimya", 155]
#df_ögretmenler["Rıza"] = [70, "erkek", "matematik", 177]
#
#print(df_ögretmenler)
#print("_"*50)
#
#df_ögretmenler["Hanife"] = [80, "kadın", "felsefe", 162]
#print(df_ögretmenler)
#print("_"*50)
#
#df_ögretmenler["Nurullah"] = [90, "erkek", "fransızca", 187]
#print(df_ögretmenler)
#print("_"*50)
#
#df_ögretmenler["Ayten"] = df_ögretmenler["Hanife"] + df_ögretmenler["Nurullah"]
#print(df_ögretmenler)
#print("_"*50)

#df_ögretmenler["Abdullah"] = df_ögretmenler["Tolga"] + df_ögretmenler["Rıza"] + df_ögretmenler["Elif"]
#print(df_ögretmenler)
#print("_"*50)
#
#
#df_ögretmenler["Abdullah"] = [35, "erkek", "ingilizce", 185]
#print(df_ögretmenler)

#ögretmenler = {"Tolga": pd.Series(data=[40, "erkek", "tarih", 180],
#                                  index=["yaş", "cinsiyet", "branş", "boy"]),
#
#               "Elif": pd.Series(data=[39, "kadın", "edebiyat", 165],
#                                 index=["yaş", "cinsiyet", "branş", "boy"]),
#
#               "Rıza": pd.Series(data=[44, "erkek", "türkçe", 173],
#                                 index=["yaş", "cinsiyet", "branş", "boy"])}

#df_ögretmenler = pd.DataFrame(ögretmenler)
#print(df_ögretmenler)
#print("_"*50)
#
#yeni_satir1 = pd.DataFrame({"Tolga": "çubuk", "Elif": "önder", "Rıza": "erdemir"},
#                           index=["soyisim"])
#
#df_ögretmenler = df_ögretmenler._append(yeni_satir1)
#
#print(df_ögretmenler)
#print("_"*50)
#
#yeni_satir2 = pd.DataFrame({"Tolga": "artvin", "Elif": "denizli", "Rıza": "kocaeli"},
#                           index=["memleket"])
#
#df_ögretmenler = df_ögretmenler._append(yeni_satir2)
#
#print(df_ögretmenler)
#print("_"*50)

#yeni_satir3 = pd.DataFrame({"Tolga": "balık tutmak", "Elif": "film izlemek", "Rıza": "spor yapmak"},
#                           index=["hobi"])
#
#df_ögretmenler = df_ögretmenler._append(yeni_satir3)
#
#print(df_ögretmenler)
#print("_"*50)
#
#yeni_satir4 = pd.DataFrame({"Tolga": 35000, "Elif": 35500, "Rıza": 36250}, index=["maaş"])
#
#df_ögretmenler = df_ögretmenler._append(yeni_satir4)
#
#print(df_ögretmenler)
#print("_"*50)

#df_ögretmenler.pop("Tolga")
#
#print(df_ögretmenler)
#print("_"*50)
#
#df_ögretmenler.pop("Elif")
#
#print(df_ögretmenler)
#print("_"*50)
#
#df_ögretmenler.pop("Rıza")
#
#print(df_ögretmenler)

#df_ögretmenler.drop("Tolga", inplace=True, axis=1)
#
#print(df_ögretmenler)

#df_ögretmenler.drop(["Tolga", "Rıza"], axis=1, inplace=True)
#
#print(df_ögretmenler)

#df_ögretmenler.drop(["Elif", "Tolga"], axis=1, inplace=True)
#
#print(df_ögretmenler)

#df_ögretmenler.drop("hobi", axis=0, inplace=True)
#
#print(df_ögretmenler)
#print("_"*50)
#
#df_ögretmenler.drop("yaş", axis=0, inplace=True)
#
#print(df_ögretmenler)
#print("_"*50)
#
#df_ögretmenler.drop(["maaş", "memleket"], axis=0, inplace=True)
#print(df_ögretmenler)
#print("_"*50)
#
#df_ögretmenler.drop(["cinsiyet", "soyisim", "branş", "boy"], axis=0, inplace=True)
#print(df_ögretmenler)
#
#df_ögretmenler.drop(["Tolga", "Elif", "Rıza"], axis=1, inplace=True)
#print(df_ögretmenler)











