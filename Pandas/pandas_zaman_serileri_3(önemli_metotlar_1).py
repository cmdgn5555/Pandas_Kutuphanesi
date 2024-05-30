import time

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

tarih = pd.to_datetime("2019/09/22")
print(tarih)
print(type(tarih))

print("\n\n")

tarihler = ["2024-Jan-18", "2024-Jan-16", "2024-Jan-10", "2024-Jan-23"]

tarih2 = pd.to_datetime(tarihler)
print(tarih2)
print("\n\n")

tarih3 = pd.to_datetime("03/07/2019")
print(tarih3)
print()

tarih4 = pd.to_datetime("2020/10/26")
print(tarih4)
print()

tarih5 = pd.to_datetime("12/15/2019", yearfirst=False)
print(tarih5)
print()

tarih6 = pd.to_datetime("01/08/2019", dayfirst=True)
print(tarih6)
print()

tarih7 = pd.to_datetime("18*10*2019", format="%d*%m*%Y")
print(tarih7)
print()

tarih8 = pd.to_datetime("23&06&2019", format="%d&%m&%Y")
print(tarih8)
print()

tarih9 = pd.to_datetime("21=11=2019=23=35=17", format="%d=%m=%Y=%H=%M=%S")
print(tarih9)
print(type(tarih9))

tarihler2 = ["may 10, 2019", "apr 15, 2019", "sep 26 2019", "jan 30 2019", "abc"]

tarih10 = pd.to_datetime(tarihler2, errors="coerce")
print(tarih10)
print()

tarih11 = pd.to_datetime(tarihler2, errors="ignore")
print(tarih11)

print("\n\n\n\n")

t = 1600000000
tarih12 = pd.to_datetime(t, unit="s")
print(tarih12)

print("\n\n")

aralık = pd.date_range("2024-01-23", "2024-01-26", freq="11h")
print(aralık)
print("\n\n")

her_ayın_son_pazarı = pd.date_range("2024-01-01", "2024-12-31", freq="WOM-4SUN")
print(her_ayın_son_pazarı)
print()

her_ayın_ilk_cuması = pd.date_range("2024-01-01", "2024-12-31", freq="WOM-1FRI")
print(her_ayın_ilk_cuması)
print()

her_ayın_ikinci_carsambası = pd.date_range("2024-01-01", "2024-12-31", freq="WOM-2WED")
print(her_ayın_ikinci_carsambası)
print()

her_ayın_ücüncü_persembesi = pd.date_range("2024-01-01", "2024-12-31", freq="WOM-3THU")
print(her_ayın_ücüncü_persembesi)

print("\n\n\n")

p = pd.Period(2020)
print(p)
print()
print(dir(p))
print()
print(p.start_time)
print()
print(p.dayofyear)
print()
print(p.daysinmonth)
print()
print(p.hour)
print()
print(p.is_leap_year)
print()
print(p.day)
print()
print(p.minute)
print()
print(p.ordinal)
print()
print(p.end_time)
print("\n\n\n\n\n")

aylık = pd.Period("2020-05", freq="M")
print(aylık)
print()
print(aylık.start_time)
print()
print(aylık.end_time)

print("_"*50)

günlük = pd.Period("2024-06-20", freq="D")
print(günlük)
print()
print(günlük.start_time)
print()
print(günlük.end_time)

print("_"*50)

haftalık = pd.Period("2024-03-11", freq="W")
print(haftalık)
print()
print(haftalık.start_time)
print()
print(haftalık.end_time)

print("_"*50)

yıllık = pd.Period("2022", freq="Y")
print(yıllık)
print()
print(yıllık.start_time)
print()
print(yıllık.end_time)

print("_"*50)

print(aylık + 10)
print()
print(aylık - 15)
print()
print(günlük + 12)
print()
print(haftalık + 5)
print()
print(yıllık + 20)
print()
print(yıllık - 30)

print("_"*50)

print(p - pd.Period(1990))
print("\n\n")

aralık2 = pd.period_range("2019-01-01", "2019-08-30", freq="M")
print(aralık2)
print()

seri = pd.Series(data=range(10, 18), index=aralık2)
print(seri)

print("\n\n")

p1 = pd.Period("2024", freq="A-DEC")
print(p1)
print()

print(p1.asfreq("M", how="start"))
print()
print(p1.asfreq("M", how="end"))
print()
print(p1.asfreq("W", how="start"))
print()
print(p1.asfreq("W", how="end"))
print()
print(p1.asfreq("D", how="start"))
print()
print(p1.asfreq("D", how="end"))

print("\n\n")

p2 = pd.Period("2019Q4")
print(p2)
print()

print(p2.start_time)
print()
print(p2.end_time)

print("\n\n")

p3 = pd.Period("2019Q3")
print(p3)
print()

print(p3.start_time)
print()
print(p3.end_time)

print("\n\n")

p4 = pd.Period("2019Q2")
print(p4)
print()

print(p4.start_time)
print()
print(p4.end_time)

print("\n\n")

p4 = pd.Period("2019Q1")
print(p4)
print()

print(p4.start_time)
print()
print(p4.end_time)


print("\n\n")

aralık3 = pd.period_range("2024Q3", "2025Q4", freq="Q-JAN")
print(aralık3)

print("\n\n")

aralık4 = pd.date_range("2020-01-01", periods=5, freq="M")
print(aralık4)
print("_"*50)
zs = pd.Series(range(len(aralık4)), index=aralık4)
print(zs)
print()
print(zs.index)

print("\n\n")

aralık5 = pd.date_range("2024-01-01", periods=15, freq="W")
print(aralık5)
print("_"*50)
zs2 = pd.Series(range(len(aralık5)), index=aralık5)
print(zs2)
print()
print(zs2.index)

print("\n\n")

aralık6 = pd.date_range("2024-01-01", periods=25, freq="D")
print(aralık6)
print("_"*50)
zs3 = pd.Series(range(len(aralık6)), index=aralık6)
print(zs3)
print()
print(zs3.index)

print("\n\n")

aralık7 = pd.date_range("2024-01-01", periods=13, freq="Y")
print(aralık7)
print("_"*50)
zs4 = pd.Series(range(len(aralık7)), index=aralık7)
print(zs4)
print()
print(zs4.index)

















