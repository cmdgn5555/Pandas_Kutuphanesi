
import pandas as pd
import numpy as np
from datetime import datetime

tarih = [datetime(2024, 1, 5), datetime(2024, 1, 10),
         datetime(2024, 1, 15), datetime(2024, 1, 20),
         datetime(2024, 1, 25)]

zaman_serisi = pd.Series(np.random.randint(100, 150, size=(5, )), index=tarih)
print(zaman_serisi)
print()
print(zaman_serisi.index)
print()
zaman_damgası = pd.to_datetime("03/06/2024")
print(zaman_damgası)
print()
print(type(zaman_damgası))
print()
dates = pd.to_datetime([datetime(2005, 9, 6),
                        "2005-Sep-7", "20050908"])
print(dates)
print()

dates2 = pd.to_datetime([datetime(2030, 10, 15, 23, 55, 40),
                         "20300105223517"])
print(dates2)
print()

dates3 = pd.to_datetime(["20240112211215", "20240222171338",
                         "20240310140346", "20240430134534"])
print(dates3)
print()
print(dates3.to_period("W"))
print()
print(dates3.to_period("D"))
print()
print(dates3.to_period("M"))
print()
print(dates3.to_period("Y"))
print()
print(dates3.to_period("M"))
print()

dates4 = pd.to_datetime(["2024-Jan-13", "2024-Jan-17",
                         "2024-Jan-23", "2024-Jan-31"])

print(dates4)
print()
print(dates4 - dates4[0])
print()

yayılma_aralığı = pd.date_range("2024-02-11", "2024-03-15")
print(yayılma_aralığı)
print()
print(len(yayılma_aralığı))
print()

per = pd.date_range("2024-05-04", periods=12, freq="D")
print(per)
print(type(per))
print()

per2 = pd.date_range("2024-03-22", periods=30, freq="H")
print(per2)
print()

per3 = pd.date_range("2024-01-01", periods=8, freq="M")
print(per3)
print()

per4 = pd.period_range("2024-02", periods=15, freq="M")
print(per4)
print(type(per4))
print()

per5 = pd.period_range("2024-08-01", periods=15, freq="H")
print(per5)
print()

per6 = pd.period_range("2024-08-01", periods=15, freq="H")
print(per6)
print()

per7 = pd.period_range("2024-5", periods=20, freq="M")
print(per7)
print()

t_delta = pd.timedelta_range(start="1 day", end="5 days", freq="3H")
print(t_delta)
print(type(t_delta))
print()

t_delta2 = pd.timedelta_range("1 day", periods=20, freq="5H")
print(t_delta2)

print("_"*500)

print(zaman_serisi)
print()

damga = zaman_serisi.index[-1]
print(damga)
print()
print(zaman_serisi[damga])
print()
print(zaman_serisi["2024-01-05"])
print()

damga2 = zaman_serisi.index[2]
print(damga2)
print()
print(zaman_serisi[damga2])
print()
print(zaman_serisi["2024-01-20"])

print("_"*500)

uzun_zaman_serisi = pd.Series(data=np.random.rand(100),
                              index=pd.date_range("1/1/2024",
                              periods=100))

print(uzun_zaman_serisi.to_string())
print()
print(uzun_zaman_serisi.head())
print()
print(uzun_zaman_serisi["2024"].to_string())
print()
print(uzun_zaman_serisi["2024-02"])
print()
print(uzun_zaman_serisi[datetime(2024, 3, 13):].to_string())
print()
print(uzun_zaman_serisi[datetime(2024, 3, 15): datetime(2024, 3, 22)])
print()
print(uzun_zaman_serisi[datetime(2024, 2, 5): datetime(2024, 2, 26):4])
print()
print(uzun_zaman_serisi.truncate(after="2024/1/10"))
print()
print(uzun_zaman_serisi.truncate(before="2024/4/1"))

print("_"*500)

tarih = pd.date_range("1/1/2024", periods=16, freq="W-Fri")
print(tarih)
print()

uzun_df = pd.DataFrame(np.random.randn(16, 4),
                       index=tarih,
                       columns=list("ABCD"))

print(uzun_df)
print()
print(uzun_df.head())
print()
print(uzun_df.loc["2024-03"])
print()
print(uzun_df.loc["2024-02"])

print("_"*500)

tarih2 = pd.DatetimeIndex(["1/5/24", "1/2/24", "1/2/24",
                           "1/5/24", "1/3/24", "1/5/24",
                           "1/3/24", "1/2/24", "1/2/24",
                           "1/5/24", "1/5/24", "1/3/24"])

print(tarih2)
print()

zaman_serisi2 = pd.Series(data=np.arange(12), index=tarih2)
print(zaman_serisi2)
print()
print(zaman_serisi2.index.is_unique)
print()
grupla = zaman_serisi2.groupby(level=0)
print(grupla.count())
print()
print(grupla.value_counts())
print()
print(grupla.mean())
print()
print(grupla.sum())
print()
print(grupla.prod())





