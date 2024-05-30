
import pandas as pd
import numpy as np

maas_df = pd.read_csv("maas veri.csv")

#print(maas_df.sort_values("Age").to_string())
#print(maas_df.sort_values(by="Salary", ascending=False).to_string())
#mask = maas_df.sort_values(by="Years of Experience", ascending=True, na_position="first", inplace=True)
#print(maas_df.to_string())

#mask = maas_df.sort_values(by="Salary", inplace=True, ascending=False, na_position="first")
#print(maas_df.to_string())

#mask = maas_df.sort_index(inplace=True, ascending=False)
#print(maas_df.to_string())

#mask = maas_df.sort_index(inplace=True, ascending=True)
#print(maas_df.to_string())

#print(maas_df.nlargest(15, "Age").to_string())
#print(maas_df.nlargest(10, "Salary").to_string())
#print(maas_df.nlargest(20, "Years of Experience").to_string())

#print(maas_df.nsmallest(25, "Age").to_string())
#print()
#print(maas_df.nsmallest(30, "Salary").to_string())
#print()
#print(maas_df.nsmallest(200, "Years of Experience").to_string())

#print(maas_df.nlargest(10, "Age").reset_index(drop=True).to_string())
#print(maas_df.nsmallest(10, "Salary").reset_index(drop=True).to_string())
#print(maas_df.nlargest(20, "Years of Experience").reset_index(drop=True).to_string())
#print(maas_df.nsmallest(30, "Age").reset_index(drop=True).to_string())

s = pd.Series(data=range(6),
              index=["d", "b", "e", "a", "c", "f"])

print(s)
print()
print(s.sort_index())
print()
print(s.sort_index(axis=0, ascending=False))
print()
print(s.sort_index(ignore_index=True))
print("_"*300)

df = pd.DataFrame(data=np.arange(12).reshape(3, 4),
                  index=["üç", "bir", "iki"],
                  columns=["b", "d", "a", "c"])

print(df)
print()
print(df.sort_index())
print()
print(df.sort_index(axis=1))
print()
print(df.sort_index(ascending=False, axis=1))
print("_"*200)

s1 = pd.Series([7, np.nan, 9, None, -8, pd.NA, -6])
print(s1)
print()
print(s1.sort_values())
print()
print(s1.sort_values(ascending=False))
print()
print("_"*200)

df2 = pd.DataFrame({"a": [7, -4, 11, 15, -9],
                    "b": [3, 10, -6, -14, 5],
                    "c": [2, 1, 8, -3, -5]})

print(df2)
print()
print(df2.sort_values(by="c"))
print()
print(df2.sort_values(by="a"))
print()
print(df2.sort_values(by="b"))

print("_"*500)

dosya = pd.read_csv("vgsalesGlobale.csv")
print(dosya.head(10).to_string())
print("_"*100)

print(dosya["Name"].head(10).sort_values())
print()
print(dosya["Year"].head(10).sort_values(ascending=False))
print()
print(dosya.sort_values(by="Rank", ascending=False))
print()
print(dosya[["Year", "Name"]].head(30).sort_values(by="Year", ascending=True))
print()
print(dosya["EU_Sales"].head(20).sort_values(ascending=False, ignore_index=True))
print()
print(dosya["Year"].nlargest(10).reset_index())
print()
print(dosya["Year"].nsmallest(20).reset_index())











