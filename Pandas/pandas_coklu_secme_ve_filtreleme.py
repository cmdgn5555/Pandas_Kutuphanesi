
import pandas as pd
import numpy as np

film = pd.read_csv("http://bit.ly/imdbratings")
print(film)
print()
print(film.head(10).to_string())
print()
print(film["title"].head())
print()
print(film[["title", "genre"]].head())
print()
print(film.loc[[1, 2, 4]].to_string())
print()
print(film.loc[3])
print()
print(film.loc[2:6].to_string())
print()
print(film.loc[5:9, "title"])
print()
print(film.loc[3:5, "duration"])
print()
print(film.loc[6:8, ["title", "genre", "star_rating"]])
print()
print(film.loc[3:6, "star_rating":"duration"].to_string())
print()
print(film.loc[:, "star_rating":"genre"].to_string())
print()
print(film.loc[film["genre"] == "Crime"].to_string())
print()
print(film.loc[film["genre"] == "Western"].to_string())
print()
print(film.loc[film["content_rating"] == "NOT RATED"].to_string())
print()
print(film.loc[film["genre"] == "Western", "title"].to_string())
print()
print(film.loc[film["genre"] == "Biography", ["title", "duration"]].to_string())
print()
print(film.loc[film["genre"] == "Animation", ["star_rating", "genre", "duration", "actors_list"]].to_string())
print()
print(film.loc[film["genre"] == "Comedy", "title":"duration"].to_string())
print()
print(film.loc[film["star_rating"] == 8.3, "star_rating":"duration"].to_string())
print()
print(film.iloc[:, 5])
print()
print(film.iloc[:, 3].head())
print()
print(film.iloc[:, 2: 4].head())
print()
print(film.columns)
print()
print(film.iloc[:, [1, 5]])
print()
print(film.iloc[:, [2, 3]])
print()
print(film.iloc[0:4, 1:4])
print()
print(film.iloc[2:5, :].to_string())
print()
print(film[(film["duration"] > 200) & (film["genre"] == "Crime")].to_string())
print()
print(film[(film["star_rating"] > 8.5) & (film["genre"] == "Action")].to_string())
print()
print(film[(film["content_rating"] == "R") & (film["genre"] == "Adventure")].to_string())
print()
print(film[(film["genre"] == "Biography") | (film["genre"] == "Western")].to_string())
print()
print(film[(film["star_rating"] == 8.3) | (film["star_rating"] == 8.1)].to_string())
print()
print(film[film["title"].isin(["The Godfather"])].to_string())
print()
print(film[film["star_rating"].isin([8.5, 9.0])].to_string())
print()
print(film[film["content_rating"].isin(["PG-13", "NOT RATED"])].to_string())
print()
print(film[film["genre"].isin(["Biography", "Western", "Adventure"])].to_string())