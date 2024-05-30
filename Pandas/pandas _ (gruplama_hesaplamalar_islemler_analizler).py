import pandas as pd

maas_df = pd.read_csv("maas veri.csv")
#print(maas_df.to_string())
#print()
#print(maas_df.describe())
#print()
#print(maas_df["Age"].head().mean())
#print()
#print(maas_df["Salary"].tail(10).mean())
#print()
#print(maas_df["Years of Experience"].head().median())
#print()
#print(maas_df["Salary"].tail(6).median())
#print()
#print(maas_df["Age"].head(8).median())
#print()
#print(maas_df["Salary"].tail(7).median())
#print()
#print(maas_df["Years of Experience"].max())
#print()
#print(maas_df["Age"].min())
#print()
#print(maas_df["Salary"].head().min())
#print()
#print(maas_df["Salary"].tail().max())
#print()
#print(maas_df["Gender"].value_counts())
#print()
#print(maas_df["Gender"].value_counts()["Male"])
#print()
#print(maas_df["Gender"].value_counts()["Female"])
#print()
#print(maas_df["Gender"].value_counts()["Other"])
#print()
#print(maas_df["Education Level"].value_counts())
#print()
#print(maas_df["Education Level"].value_counts()["High School"])
#print()
#print(maas_df["Job Title"].value_counts().to_string())
#print()
#print(maas_df["Job Title"].value_counts()["Full Stack Engineer"])
#print()
#print(maas_df["Job Title"].value_counts()["Product Manager"])
#print()
#print(maas_df["Education Level"].value_counts())
#print()
#print(maas_df["Education Level"].value_counts(normalize=True) * 100)
#print()
#print(maas_df["Gender"].value_counts(ascending=False, normalize=True) * 100)
#print()
#print(maas_df["Age"].head(4).sum())
#print()
#print(maas_df["Salary"].tail().sum())
#print()
#print(maas_df["Years of Experience"].tail(3).sum())
#print()
#print(maas_df["Salary"].head(10).sum())
#print()
#print(maas_df.groupby(by="Job Title")["Age"].sum())
#print("_"*50)
#print(maas_df.groupby(by="Gender")["Salary"].mean())
#print()
#print(maas_df.groupby(by="Education Level")["Years of Experience"].mean())
#print("_"*100)

#maas_df["Age"] = maas_df["Age"].apply(lambda x: x - 5)
#print(maas_df["Age"].head())
#print("_"*50)
#maas_df["Years of Experience"] = maas_df["Years of Experience"].apply(lambda x: x * 2)
#print(maas_df["Years of Experience"].head())
#print("_"*50)
#maas_df["Salary"] = maas_df["Salary"].apply(lambda x: x + 50)
#print(maas_df["Salary"].head())
#print("_"*50)

#maas_df["Age"] = maas_df["Age"].apply(lambda x: x * 3 if x > 35 else x)
#print(maas_df["Age"].head())
#print("_"*50)
#maas_df["Years of Experience"] = maas_df["Years of Experience"].apply(lambda x: x**2 if x < 10 else x)
#print(maas_df["Years of Experience"].head())
#print("_"*50)
#maas_df["Salary"] = maas_df["Salary"].apply(lambda x: x / 2 if x < 100000 else x)
#print(maas_df["Salary"].head())
#maas_df["Education Level"] = maas_df["Education Level"].apply(lambda x: x.upper() if x == "Master's" else x)
#print(maas_df["Education Level"].head(10))
#maas_df["Education Level"] = maas_df["Education Level"].apply(lambda x: x.lower() if x == "Bachelor's" else x)
#print(maas_df["Education Level"].head(10))
#maas_df["Education Level"] = maas_df["Education Level"].apply(lambda x: x.replace("PhD", "High School") if x == "PhD" else x)
#print(maas_df["Education Level"].head(10))
#maas_df["Gender"] = maas_df["Gender"].apply(lambda x: x.replace("Male", "erkek") if x == "Male" else x)
#print(maas_df["Gender"].head(10))
#maas_df["Gender"] = maas_df["Gender"].apply(lambda x: x.replace("Female", "bayan") if x == "Female" else x)
#print(maas_df["Gender"].head(10))
#print("_"*50)

#print(maas_df.groupby(by="Gender").apply(lambda x: x["Age"].mean()))
#print()
#print(maas_df.groupby(by="Education Level").apply(lambda x: x["Salary"].sum()))
#print()
#print(maas_df.groupby(by="Job Title").apply(lambda x: x["Salary"].sum()))
#print("_"*200)
#
#print(maas_df.groupby(by="Gender").apply(lambda x: x["Years of Experience"].mean()))
#print()
#print(maas_df.groupby(by="Education Level").apply(lambda x: x["Years of Experience"].sum()))
#print()
#print(maas_df.groupby(by="Job Title").apply(lambda x: x["Salary"] * 2))
#print()
#print(maas_df.groupby(by="Gender").apply(lambda x: x["Salary"] + 1000))




















