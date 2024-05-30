
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("maas veri.csv")

print(df.to_string())
print("_"*100)

#maas_group = df.groupby("Job Title")["Age"].mean().reset_index()

#print(maas_group.to_string())
#print("_"*100)

#maas_group.sort_values("Age", ascending=False).head(10).plot(x="Job Title", y="Age", kind="barh")

#plt.show()


#maas_group = df.groupby("Education Level")["Salary"].sum().reset_index()
#print(maas_group.to_string())
#print("_"*100)
#
#maas_group.sort_values("Salary", ascending=False).head(10).plot(x="Education Level", y="Salary", kind="barh")
#
#plt.show()

#maas_group = df.groupby("Gender")["Salary"].sum().reset_index()
#print(maas_group.to_string())
#print("_"*100)
#
#maas_group.plot(x="Gender", y="Salary", kind="barh")
#
#plt.show()

#maas_group = df.groupby("Gender")["Years of Experience"].sum().reset_index()
#print(maas_group.to_string())
#
#maas_group.plot(x="Gender", y="Years of Experience", kind="barh")
#
#plt.show()

#maas_group = df.groupby("Job Title")["Age"].mean().reset_index()
#print(maas_group.to_string())
#print()
#
#maas_group.plot(x="Job Title", y="Age", kind="barh")
#
#plt.show()

#maas_group = df.groupby("Education Level")["Age"].count().reset_index()
#print(maas_group.to_string())
#print()
#
#maas_group.plot(x="Education Level", y="Age", kind="barh")
#
#plt.show()

#maas_group = (df.groupby("Gender")["Salary"].mean() / 2).reset_index()
#print(maas_group.to_string())
#print()
#
#maas_group.plot(x="Gender", y="Salary", kind="barh")
#
#plt.show()

#maas_group = (df.groupby(by="Education Level")["Years of Experience"].sum() * 5).reset_index()
#print(maas_group.to_string())
#print()
#
#maas_group.plot(x="Education Level", y="Years of Experience", kind="barh")
#
#plt.show()


