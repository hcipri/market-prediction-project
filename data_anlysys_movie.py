# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

netflix_df = pd.read_csv("netflix_data.csv")
filtering = (netflix_df['release_year'] <= 1999) & (netflix_df['release_year'] > 1989)
netflix_filter = netflix_df[filtering]

short_movie_count = 0

for index, row in netflix_filter.iterrows():
    if row['duration'] < 90:
        if row['genre']=="Action":
            short_movie_count += 1
duration=95
print()
print(short_movie_count)
plt.hist(netflix_filter['duration'], bins=30)
plt.show()
print(netflix_df)
print(netflix_filter)

