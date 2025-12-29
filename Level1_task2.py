#import panda
import pandas as pd

# Load dataset
ds = pd.read_csv("Dataset .csv")   # use your exact file name

# 1. City with highest number of restaurants
city_count = ds['City'].value_counts()
top_city = city_count.idxmax()

# 2. Average rating for each city
avg_rating_city = ds.groupby('City')['Aggregate rating'].mean()

# 3. City with highest average rating
highest_avg_rating_city = avg_rating_city.idxmax()

# Print results
print("City with highest number of restaurants:", top_city)
print("City with highest average rating:", highest_avg_rating_city)
