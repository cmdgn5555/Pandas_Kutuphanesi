
import pandas as pd
import numpy as np


#dosya = pd.read_csv("örnek dosya.csv")

#print(dosya["City"] == "Amsterdam")
#print(dosya[dosya["City"] == "Amsterdam"])

#mask = dosya["Neighbourhood"] == "Harlem"
#print(dosya[mask])
#print()

#print(dosya["Room Type"].unique())
#print()
#mask = dosya["Room Type"] == "Shared room"
#print(dosya[mask])
#print()
#print(dosya["Room Type"].value_counts())


#mask = dosya["Room Type"] == "Private room"
#print(dosya[mask])
#print()
#print(dosya["Room Type"].value_counts())

#print(dosya["Room Type"].unique())
#print()
#mask = dosya["Room Type"] != "Entire home/apt"
#print(dosya[mask])
#print()
#print(dosya["Room Type"].value_counts())

#mask1 = dosya["Room Type"] != "Entire home/apt"
#mask2 = dosya["Room Type"] != "Private room"
#mask3 = mask1 & mask2
#print(dosya[mask3])

#mask1 = dosya["Room Type"] == "Shared room"
#mask2 = dosya["Room Type"] == "Private room"
#mask3 = mask1 | mask2
#print(dosya[mask3])

#mask = (dosya["Room Price"] > 80) & (dosya["Room Price"] < 90)
#print(dosya[mask])

#mask = (dosya["Room Price"] > 550) | (dosya["Room Availability"] < 10)
#print(dosya[mask])

#mask = (dosya["Room Price"] == 500) | (dosya["Room Availability"] == 15)
#print(dosya[mask])

#mask = (dosya["Room Price"] == 95) & (dosya["Room Availability"] == 10)
#print(dosya[mask])

#mask = dosya["State"].isin(["Attica", "Berlin", "California"])
#print(dosya[mask])

#mask = dosya["Room Type"].isin(["Shared room", "Private room"])
#print(dosya[mask])

#mask = dosya["Neighbourhood"].isin(["Neubau", "Monash", "Jamaica", "Flatbush"])
#print(dosya[mask])

#print(dosya["State"].to_string())

#print(dosya["State"].to_string().count("Oregon"))

#mask = (dosya["State"].isin(["Veneto", "Oregon"]))
#print(dosya[mask])

#print(dosya["Country"].to_string().count("Italy"))

#mask = dosya["Country"].isin(["Germany", "Belgium", "Italy"])
#print(dosya[mask])

#mask = dosya["Room Price"].between(150, 160)
#print(dosya[mask])

#mask = dosya["Room Availability"].between(20, 30)
#print(dosya[mask])

#mask = dosya["Review Date"].between("2014-05-01", "2014-05-14")
#print(dosya[mask])


#print(dosya["City"].sort_values().head(50))
#print()
#print(dosya["City"].sort_values().head(50).duplicated())

#print(dosya["State"].sort_values().head(30))
#print(dosya["State"].sort_values().head(30).duplicated())

#print(dosya["Room Type"].sort_values().tail(20))
#print(dosya["Room Type"].sort_values().tail(20).duplicated())

#print(dosya["City"].sort_values().drop_duplicates().count())

#mask = ~dosya["City"].duplicated()
#print(dosya[mask])

#mask = dosya["Room Type"].describe()
#print(mask)

#mask = ~dosya["State"].duplicated()
#print(dosya[mask])

#print(len(dosya.drop_duplicates(subset=["City"])))
#print(len(dosya.drop_duplicates(subset=["Room Type"])))
#print(len(dosya.drop_duplicates(subset=["Neighbourhood"])))

#print(len(dosya["City"].unique()))
#print(dosya["City"].unique())
#print(type(dosya["City"].unique()))

#print(dosya["State"].unique())
#print()
#print(dosya["State"].nunique())

#print(dosya["City"].unique())
#print()
#print(dosya["City"].nunique())

#print(dosya["Country"].unique())
#print()
#print(dosya["Country"].nunique())

#print(dosya["Room Type"].unique())
#print()
#print(dosya["Room Type"].nunique())

#print(dosya["Neighbourhood"].unique())
#print()
#print(dosya["Neighbourhood"].nunique())

maas_df = pd.read_csv("maas veri.csv")

print(maas_df)

#print("_"*50)
#mask = maas_df["Gender"] == "Female"
#print(maas_df[mask])
#
#print("_"*50)
#mask = maas_df["Gender"] == "Male"
#print(maas_df[mask])
#
#print("_"*50)
#mask = maas_df["Job Title"] == "Sales Manager"
#print(maas_df[mask].to_string())
#
#print("_"*50)
#mask = maas_df["Education Level"] == "High School"
#print(maas_df[mask].to_string())

#mask = (maas_df["Gender"] == "Male") & (maas_df["Job Title"] == "Senior Manager")
#print(maas_df[mask].to_string())

#mask = (maas_df["Age"] > 60.0) | (maas_df["Salary"] < 15000)
#print(maas_df[mask].to_string())

#mask = (maas_df["Education Level"] == "Bachelor's Degree") & (maas_df["Years of Experience"] == 20.0)
#print(maas_df[mask].to_string())

#mask = (maas_df["Education Level"] == "Master's Degree") | (maas_df["Salary"] == 75000.0)
#print(maas_df[mask].to_string())

#mask = ~(maas_df["Gender"] == "Female")
#print(maas_df[mask].to_string())

#mask = ~(maas_df["Job Title"] == "Senior Manager")
#print(maas_df[mask].to_string())

#mask = ~((maas_df["Salary"] > 60000) & (maas_df["Salary"] < 63000))
#print(maas_df[mask].to_string())

#mask = maas_df["Job Title"].isin(["Marketing Analyst"])
#print(maas_df[mask].to_string())

#mask = maas_df["Job Title"].isin(["Product Manager", "Sales Executive"])
#print(maas_df[mask].to_string())

#mask = maas_df["Salary"].isin([140000.0, 90000.0, 55000.0])
#print(maas_df[mask].to_string())

#mask = maas_df["Years of Experience"].isin([12.0, 6.0, 11.0, 25.0])
#print(maas_df[mask].to_string())

#maas_df.at[0, "Job Title"] = None
#maas_df.at[1, "Job Title"] = pd.NA
#maas_df.at[2, "Job Title"] = np.NAN
#
#mask = maas_df["Job Title"].str.contains("Financial", na=True)
#print(maas_df[mask].to_string())

#maas_df.at[0, "Education Level"] = None
#maas_df.at[1, "Education Level"] = pd.NA
#maas_df.at[2, "Education Level"] = np.NAN
#
#mask = maas_df["Education Level"].str.contains("School", na=True)
#print(maas_df[mask].to_string())

#maas_df.at[0, "Job Title"] = None
#maas_df.at[1, "Job Title"] = pd.NA
#maas_df.at[2, "Job Title"] = np.NAN
#
#mask = maas_df["Job Title"].str.contains("Associate", na=False)
#print(maas_df[mask].to_string())

#mask = maas_df["Age"] <= 22
#print(maas_df[mask])

#mask = maas_df["Salary"] >= 240000
#print(maas_df[mask])

#mask = maas_df["Age"] != 32
#print(maas_df[mask].to_string())

#mask = maas_df["Salary"] != 250000
#print(maas_df[mask].to_string())

#mask = maas_df["Job Title"] != "Software Engineer"
#print(maas_df[mask].to_string())

#mask = maas_df["Job Title"] > "T"
#print(maas_df[mask].to_string())

#mask = maas_df["Education Level"] < "C"
#print(maas_df[mask].to_string())

#mask = maas_df["Gender"] > "K"
#print(maas_df[mask].to_string())

#mask = maas_df["Gender"] < "J"
#print(maas_df[mask].to_string())

obje = pd.Series(np.arange(10, 20), index=list("abcdefghjk"))
print(obje)
print(obje["j"])
print()
print(obje[4])
print()
print(obje[5:9])
print()
print(obje[["b", "d", "a"]])
print()
print(obje[[3, 7, 9]])
print()
print(obje[obje < 15])
print()
print(obje[obje > 13])
print()
print(obje["c": "g"])
print()
obje["a": "d"] = 8
print(obje)
print()
obje[6: 9] = 4
print(obje)
print("_"*200)

veri = pd.DataFrame(np.arange(25).reshape(5, 5),
                    index=["rusya", "ispanya", "almanya", "türkiye", "amerika"],
                    columns=["bir", "iki", "üç", "dört", "beş"])

print(veri)
print()
print(veri["dört"])
print()
print(veri[["bir", "iki"]])
print()
print(veri[:4])
print()
print(veri[1:3])
print()
print(veri["rusya": "almanya"])
print()
print(veri[veri["iki"] > 10])
print()
print(veri[veri["dört"] < 9])
print()
print(veri[veri["bir"] == 5])
print()
veri[veri < 7] = 0
print(veri)
print()
veri[veri > 20] = 30
print(veri)
print()
print(veri.iloc[3])
print()
print(veri.iloc[4, [0, 1, 3]])
print()
print(veri.iloc[2, [1, 2, 4]])
print()
print(veri.iloc[[2, 3], [2, 3, 4]])
print()
print(veri.iloc[[0, 4], [0, 2, 4]])
print()
print(veri.loc["amerika", ["iki", "üç"]])
print()
print(veri.loc["ispanya", ["bir", "beş"]])
print()
print(veri.loc[["almanya", "rusya"], ["iki", "üç"]])
print()
print(veri.loc[["türkiye", "ispanya", "amerika"], ["bir", "üç", "beş"]])
print()
print(veri.loc[:"türkiye", "beş"])
print()
print(veri.loc["ispanya":, "iki"])




























