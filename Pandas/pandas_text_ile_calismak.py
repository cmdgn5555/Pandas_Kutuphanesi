import pandas as pd
import numpy as np

#dosya = pd.read_csv("örnek dosya.csv")

#print(dosya["Country"])
#print("_"*50)
#print(dosya["Country"].str.upper())
#print("_"*50)
#print(dosya["Country"].str.lower())
#print("_"*50)
#print(dosya["Country"].str.title())

#print(dosya["State"].str.upper().str.lower().str.title())
#print(dosya["City"].str.lower().str.capitalize().str.upper())

#print(dosya["City"].head(10))
#print()
#print(dosya["City"].head(10).str.len())

#print(dosya["Country"].tail(10))
#print()
#print(dosya["Country"].tail(10).str.len())

#print(dosya["Neighbourhood"].head())
#print()
#print(dosya["Neighbourhood"].head().str.len())

#print(dosya["Neighbourhood"].tail())
#print()
#print(dosya["Neighbourhood"].tail().str.len())

#print(dosya["City"].head(20))
#print()
#print(dosya["City"].head(20).str.replace("N", "S"))

#print(dosya["City"].head(20))
#print()
#print(dosya["City"].head(20).str.replace("New", "Yeni"))

#print(dosya["City"].head(20))
#print()
#print(dosya["City"].head(20).str.replace("L", "B"))

#print(dosya["State"].head(50))
#print()
#print(dosya["State"].head(50).str.replace("California", "Ankara"))

#print(dosya["City"].head(20))
#print()
#print(dosya["City"].head(20).str.contains("York"))

#print(dosya["City"].tail(30))
#print()
#print(dosya["City"].tail(30).str.upper().str.contains("NEW"))

#print(dosya["Country"].tail(30))
#print()
#print(dosya["Country"].tail(30).str.upper().str.contains("UNITED"))

#print(dosya["State"].tail(50))
#print()
#print(dosya["State"].tail(50).str.lower().str.contains("england"))

#print(dosya["Room Type"].head(50))
#print()
#print(dosya["Room Type"].head(50).str.lower().str.replace("room", "ROOM").str.contains("ROOM"))

#print(dosya["Review Content"].head(20))
#print()
#print(dosya["Review Content"].head(20).str.upper().str.contains("ANNABEL"))

#print(dosya["Review Content"].tail(20))
#print()
#print(dosya["Review Content"].tail(20).str.lower().str.contains("ysaira and jose"))

#mask = dosya["City"].str.lower().str.contains("london")
#print(dosya[mask].head(10))

#mask = dosya["Room Type"].str.lower().str.contains("shared")
#print(dosya[mask])

#mask = dosya["Country"].str.upper().str.replace("GREECE", "MEXICO").str.contains("MEXICO")
#print(dosya[mask])

#print(dosya["Room Type"].head(20))
#print()
#print(dosya["Room Type"].head(20).str.upper().str.startswith("E"))

#mask = dosya["Review Content"].str.lower().str.startswith("k")
#print(dosya[mask])
#print()
#print(dosya.iloc[233])

#mask = dosya["Room Type"].str.upper().str.startswith("SHARED")
#print(dosya[mask])
#print()
#print(dosya.iloc[914])

#mask = dosya["City"].str.upper().str.endswith("ENS")
#print(dosya[mask])
#print(dosya.iloc[748])

#mask = dosya["State"].str.lower().str.endswith("madrid")
#print(dosya[mask])
#print(dosya.iloc[419])

#print(dosya["Country"].to_string())
#print()
#mask = dosya["Neighbourhood"].str.upper().str.endswith("STER")
#print(dosya[mask])
#print(dosya.iloc[502])

#print(dosya["Review Date"].head())
#print("_"*20)
#print(dosya["Review Date"].head().str.strip())

#print(dosya["Room Type"].tail(3))
#print()
#print(dosya["Room Type"].tail(3).str.strip())

#print(dosya["City"].head(20).str.split(" "))
#print(dosya["Country"].tail(30))
#print(dosya["Country"].tail(30).str.split(" "))

#for i in dosya["Review Content"].head(1).str.split(" "):
#    print(i, " ", i[5], " ", i[5][4])

#for i in dosya["Review Date"].head().str.strip().str.split("-"):
#    print("_".join(i))

#print(dosya["Country"].head())
#print(dosya["Country"].head().str.split(" ").str.get(0))

#print(dosya["Review Date"].tail())
#for i in dosya["Review Date"].tail().str.split("-").str.get(-1):
#    print(i)

#print(dosya["Room Type"].tail(10).str.strip())
#for i in dosya["Room Type"].tail(10).str.strip().str.split(" ").str.get(0):
#    print(i)

#print(dosya["Listing Title"].head())
#print()
#for i in dosya["Listing Title"].head().str.split(" ").str.get(-1):
#    print(" ".join(i))

#print(dosya["Review Date"].tail(10).str.split("-", expand=True))

veri = ["sezen", "ahmet", "nur", "yasin", np.nan]
print(veri)
print(type(veri))
print()
isim = pd.Series(veri)
print(isim)
print(type(isim))
print()
print(isim.str.capitalize())
print()
print(isim.str.lower())
print()
print(isim.str.len())
print("_"*300)

df = pd.DataFrame(data=np.random.randn(3, 2),
                  columns=["Sütun A", "Sütun B"],
                  index=range(3))

print(df)
print()
print(df.columns)
print()
print(df.columns.str.lower().str.replace(" ", "+"))
print("_"*300)

s = pd.Series(["x-y-z-r-s-v", "w-f-m-o-ö-z", np.nan, "e-a-b-g-h-l"])
print(s)
print()
print(s.str.split("-"))
print()
print(s.str.split("-").str.get(-1))
print()
print(s.str.split("-").str[0])
print()
print(s.str.split("-", expand=True, n=4))
print("_"*300)

para = pd.Series(["$20", "-$25", "$4500"])
print(para)
print()
print(para.str.replace("$", ""))
print("_"*300)

film = pd.read_csv("http://bit.ly/imdbratings")
print(film.head().to_string())
print()
print(film["title"].str.upper())
print()
print(film.columns)
print()
film.columns = film.columns.str.title()
print(film.head().to_string())
print()
print(film["Genre"].str.upper())
print()
print(film.head(10).to_string())
print()
print(film["Actors_List"].str.contains("Marlon Brando"))
print()
print(film[film["Actors_List"].str.contains("Brad Pitt")].to_string())
print()
print(film[film["Actors_List"].str.contains("Tom Cruise")].to_string())
print()
print(film[film["Actors_List"].str.contains("Jack Nicholson")].to_string())
print()
print(film["Actors_List"].str.replace("[", "").str.replace("]", "").str.replace("u", "").str.replace("'", "").str.replace(",", ""))












