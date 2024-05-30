
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

rng = pd.date_range(start="2024", end="2025", freq="BM")
print(rng)
print()
zaman_serisi = pd.Series(np.random.randn(len(rng)), index=rng)
print(zaman_serisi)
print()
print(zaman_serisi[:7])
print()
print(zaman_serisi[2:6])

print("_"*500)

fb = pd.read_csv("FB.csv", parse_dates=["Date"], index_col="Date")
print(fb.to_string())
print()
print(fb.head().to_string())
print()
print(fb.dtypes)
print()
print(fb.loc["2019-04"].to_string())
print()
print(fb.iloc[10:20, 0:2].to_string())
print()
print(fb.loc["2018-07"].head().Volume.mean())
print()
print(fb.loc["2018-07"].head().Close.sum())
print()
print(fb.loc["2019"].Open.sum())
print()
print(fb["2019-03-09":"2019-03-15"].to_string())
print()
t_stamp = pd.to_datetime("2019/07/10")
print(t_stamp)
print()
print(fb.loc[fb.index >= t_stamp, :].to_string())
print()
t_stamp2 = pd.to_datetime("2018/09/04")
print(fb.loc[fb.index < t_stamp2].to_string())
print()
print(fb.loc["2019-03"])
print("_"*500)

fb2 = pd.read_csv("FB-no-date.csv", sep=";")
print(fb2.to_string())
print()
print(fb2.head().to_string())
print()

dates = pd.date_range(start="2019/03/01", end="2019/03/29", freq="B")
print(dates)
print("\n")

fb2 = fb2.set_index(dates)
print(fb2)
print()
print(fb2.head())
print()
print(fb2.index)
print()

sütun = fb2["Close"] / 1000000
print(sütun)
print()

#sütun.plot(x="Close", y="Close", kind="barh")
#plt.show()

fb3 = fb2.asfreq("D", fill_value=123456789)
print(fb3)
print("\n")

#ciz = fb3["Close"].plot(x="Close", kind="barh")
#plt.show()

fb4 = fb2.asfreq("D", method="bfill")
print(fb4)
print()

fb5 = fb2.asfreq("D", method="ffill")
print(fb5)
print()

fb6 = fb2.asfreq("W", method="ffill")
print(fb6)
print()

fb7 = fb2.asfreq("H", method="pad")
print(fb7.to_string())
print()

sütun2 = fb7["Open"] / 1000000
print(sütun2.to_string())
print()

#sütun2.plot()
#plt.show()

print("\n\n\n")

z = pd.date_range(start="2019/03/01", periods=60, freq="B")
print(z)
print()

z1 = pd.date_range(start="2019/03/01", periods=30, freq="W")
print(z1)

z2 = pd.date_range(start="2000/04/01", periods=20, freq="B")

print("\n\n\n")

zs = pd.Series(np.random.randint(1, 10, len(z1)), index=z1)
print(zs)
print("\n")

zs2 = pd.Series(np.random.randint(1, 10000, len(z2)), index=z2)
print(zs2)

zs2.plot(kind="bar")
plt.show()











