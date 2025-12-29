
import pandas as ps
ds=ps.read_csv("Dataset .csv")
print(ds['Cuisines'].head())
#most common cuisine combination
cuisin_comb=ds['Cuisines'].value_counts().head(10)
print(cuisin_comb)
#maximum cuisin combination
max_comb_cuisin=cuisin_comb.idxmax()
print("most common cuisin",max_comb_cuisin)
#averagerating for top cuisines
top_cuisines = cuisin_comb.index

avg_ratings_by_cuisine = (
    ds[ds['Cuisines'].isin(top_cuisines)]
    .groupby('Cuisines')['Aggregate rating']
    .mean()
    .sort_values(ascending=False)
)

print(avg_ratings_by_cuisine)
#tope rating for cuisin
high_rating_cuisines = avg_ratings_by_cuisine[avg_ratings_by_cuisine >= 3.7]
print(high_rating_cuisines)
