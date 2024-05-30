
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pytz
import datetime as dt

fb = pd.read_csv("FB.csv", parse_dates=["Date"], index_col="Date")
print(fb.to_string())
print("_"*50)
print(fb.head().to_string())
print("_"*50)
print(fb.resample("M").sum().to_string())
print("_"*50)

kapanıs = fb["Close"].resample("M").sum()
print(kapanıs.to_string())
print()
#kapanıs = fb["Close"].resample("M").sum().plot(kind="barh")
#plt.show()

sütun1 = fb["Open"] / 100
print(sütun1.to_string())
print()

acılıs = (fb["Open"] / 100).resample("W").sum().head()
print(acılıs.to_string())
print()

#acılıs = (fb["Open"] / 100).head().resample("W").sum().head().plot(y="Date", kind="bar")
#plt.show()

vol = (fb["Volume"] / 100000000).resample("M").sum()
print(vol)

#vol = (fb["Volume"] / 100000000).resample("M").sum().plot(kind="barh")
#plt.show()

print("\n\n\n\n")

df = pd.DataFrame(fb.Close["2019-03"])
print(df.to_string())
print()
print(df.head().to_string())
print()

print(df.shift(2))
print()
print(df.shift(-3))
print("_"*50)

df["bir önceki fiyat"] = df.shift(1)
print(df)
print()

df["bir günlük fark"] = df["Close"] - df["bir önceki fiyat"]
print(df)
print("_"*50)

df2 = df[["Close"]]
print(df2.head())
print()

print(df2.index)
print()

df2.index = pd.date_range("2019-03-01", periods=21, freq="B")
print(df2.index)
print()

print(df2.shift(-1))
print()
print(df2.shift(5, fill_value="ileri ötelendi"))

print("\n\n")

print(df2.shift(-5, fill_value="geri ötelendi"))

print("_"*50)

#print(fb["Close"].plot())
#plt.show()

print(fb["Close"].rolling(30).sum().to_string())
#fb["Close"].rolling(30).sum().plot()
#plt.show()

print("_"*50)

for tz4 in pytz.all_timezones:
    print(tz4)

print("\n\n\n\n")

tar = dt.datetime.now()
print(tar)
print()

tar2 = dt.datetime.now(pytz.utc)
print(tar2)
print()

tar3 = dt.datetime.now(pytz.timezone("Europe/London"))
print(tar3)
print()

tar4 = dt.datetime.now(pytz.timezone("America/New_York"))
print(tar4)
print()

tar5 = pytz.common_timezones[-5:]
print(tar5)
print()

for tz3 in pytz.country_timezones["us"]:
    print(tz3)

print("\n\n")

x = pd.date_range("05/30/2024 9:30", periods=6, freq="D")
print(x)
print()
zs = pd.Series(np.random.randint(10, 30, len(x)), index=x)
print(zs)
print()
print(zs.index.tz)
print()

zs_utc = zs.tz_localize("UTC")
print(zs_utc)
print()

print(zs_utc.tz_convert("Asia/Tokyo"))

print("\n\n")

z_damga = pd.Timestamp("2017-06-20 11:00")
print(z_damga)
print()

z_damga = z_damga.tz_localize("utc")
print(z_damga)
print()

print(z_damga.tz_convert("Europe/Istanbul"))
print()
print(z_damga.tz_convert("Asia/Tokyo"))
print()
print(z_damga.tz_convert("Europe/Amsterdam"))

print("\n\n\n")

zs1 = zs[:5].tz_localize("Europe/Amsterdam")
print(zs1)
print()

zs2 = zs[2:].tz_localize("Europe/Istanbul")
print(zs2)
print()

sonuc = zs1 + zs2
print(sonuc)
print()
print(sonuc.index)













