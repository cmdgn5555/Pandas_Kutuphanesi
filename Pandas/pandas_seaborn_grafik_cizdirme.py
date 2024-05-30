
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

iris = pd.read_csv("iris.txt", sep="\t")
print(iris.head())
print()
#print(iris["Canak_yaprak_boyu"].plot())
#plt.show()
print()
#print(iris.head().plot(kind="bar"))
#plt.show()

df = pd.DataFrame(np.random.randint(100, 500, size=(5, 3)),
                  index=["bir", "iki", "uc", "dort", "bes"],
                  columns=pd.Index(list("ABC")))

print(df)
print()
#df.plot.bar()
#plt.show()

#df.plot.bar(alpha=0.5, stacked=True)
#plt.show()

bahsis = sns.load_dataset("tips")
print(bahsis.to_string())
print("\n\n")
print(bahsis.head())
print("\n")
parti_say = pd.crosstab(bahsis["day"], bahsis["size"])
print(parti_say)
print("\n")
#parti_say.plot.bar()
#plt.show()
bahsis["bahsis_yüzde"] = bahsis["tip"] / (bahsis["total_bill"] - bahsis["tip"])
print(bahsis.head())
#sns.barplot(x="day", y="bahsis_yüzde", data=bahsis, orient="v", hue="sex")
#plt.show()
print("\n\n")
#bahsis["bahsis_yüzde"].plot.hist(bins=70)
#plt.show()
sns.distplot(bahsis["bahsis_yüzde"], bins=30, color="r")
#plt.show()
