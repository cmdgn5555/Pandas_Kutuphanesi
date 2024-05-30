import pandas as pd
from pprint import pprint

#dosya = pd.read_csv("örnek dosya.csv")

#print(dosya)
#print()
#print(type(dosya))
#print()
#print(dosya.ndim)
#print()
#print(dosya.info())
#print()
#print(dosya.head())
#print()
#print(dosya.tail())
#print()
#print(dosya.dtypes)
#print()
#print(dosya.columns)
#print()
#print(dosya.memory_usage())

#print(dosya.head())
#print(dosya["Room Availability"].head().sum())
#print()
#
#print(dosya.head(3))
#print(dosya["Room Price"].head(3).sum())
#print()
#
#
#
#print(dosya.tail())
#print(dosya["Room Price"].tail().sum())
#print()
#
#print(dosya.tail(3))
#print(dosya["Room Availability"].tail(3).sum())
#print()

#for i in dosya["Room Type"].unique():
#    print(i)

#for i in dosya["City"].unique():
#    print(i)

#for i in dosya["State"].unique():
#    print(i)

#for i in dosya["Country"].unique():
#    print(i)



#for i in dosya["Room Type"].drop_duplicates():
#    print(i)

#for i in dosya["City"].drop_duplicates():
#    print(i)

#for i in dosya["State"].drop_duplicates():
#    print(i)

#for i in dosya["Country"].drop_duplicates():
#    print(i)

#print(dosya.head())
#print()
#print(dosya["Room Availability"].head().add(10))
#print("_"*100)
#
#print(dosya.tail())
#print()
#print(dosya["Room Price"].tail().add(20))

#print(dosya.head(10))
#print(dosya["Room Availability"].head(10).add(1))

#print(dosya.tail(10))
#print(dosya["Room Price"].tail(10).add(2))

#print(dosya.head())
#print(dosya["Room Price"].head() + 5)

#print(dosya.tail())
#print(dosya["Room Availability"].tail() + 15)

#print(dosya.head(20))
#print(dosya["Room Availability"].head(20) + 50)

#print(dosya.tail(15))
#print(dosya["Room Price"].tail(15) + 100)

#print(dosya.head())
#print(dosya["Room Price"] * 2)

#print(dosya.tail())
#print(dosya["Room Price"].tail().mul(3))

#print(dosya.head(3))
#print(dosya["Room Availability"].head(3).div(10))

#print(dosya.tail(3))
#print(dosya["Room Availability"].tail(3) / 2)

#print(dosya.head(10))
#print(dosya["Room Price"].head(10).sub(100))

#print(dosya.tail(20))
#print(dosya["Room Price"].tail(20) - 30)

#print(dosya["City"].value_counts())

#print(dosya["Neighbourhood"].value_counts())

#print(dosya["State"].value_counts())

#print(dosya["Country"].value_counts())

#print(dosya["Room Type"].value_counts())

#print(dosya["Room Price"].sort_values(ascending=False).head(1))

#print(dosya["Room Availability"].sort_values(ascending=True).head(1))

#print(dosya["Room Price"].sort_values())
#print()
#print(dosya["Room Price"].sort_values(ascending=False))

#print(dosya["State"].sort_values())

#print(dosya["City"].sort_values(ascending=False))

#print(dosya.sort_values("Room Price", ascending=False))

#print(dosya.sort_values("Room Availability", ascending=True))

#print(dosya.sort_values("Review ID").head(10))

#print(dosya.sort_values("Review ID",ascending=False))

#print(dosya.sort_values("Review Date", ascending=True))

#print(dosya.sort_values("Review Date", ascending=False))

dosya = pd.read_csv("titanic.csv")
print(dosya.to_string())
print()
print(dosya.shape)
print()
print(dosya.dtypes)
print()
print(dosya.info())
print()
print(dosya.columns)
print()
print(dosya.index)
print("_"*100)

#yeni_veri = dosya[["survived", "age"]].head(10)
#print(yeni_veri)
#print()

#yeni_veri.to_csv("yeni_veri.csv", index=False)

#comp_opts = dict(method="zip", archive_name="yeni_veri_2.csv")
#
#yeni_veri.to_csv("data.zip", index=False, compression=comp_opts)

#yeni_veri = dosya[["embark_town", "alive", "alone"]].tail(20)
#print(yeni_veri)
#
#comp_opts = dict(method="zip", archive_name="yeni.csv")
#
#yeni_veri.to_csv("data2.zip", index=False, compression=comp_opts)

#yeni_veri = dosya[["sex", "fare"]].head(50)
#print(yeni_veri)
#
#compression_options = dict(method="zip", archive_name="yeni2.csv")
#
#yeni_veri.to_csv("data3.zip", index=True, compression=compression_options)





















