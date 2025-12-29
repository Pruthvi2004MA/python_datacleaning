#import pandas
import pandas as ps
#Reading csv 
ds=ps.read_csv("Dataset .csv")
ds.info()
#split cuisins;convert each strig into the list
ds['Cuisines'] = ds['Cuisines'].str.split(', ')
#create one row per cuisine using 'explode()' function
Row_per_cuisine=ds.explode('Cuisines')
#count each cusin
cusin_count=Row_per_cuisine['Cuisines'].value_counts()
print(cusin_count)
#top 3 cusin
top_cusin=cusin_count.head(3)
print(top_cusin)
#total percentage
total_resturant=ds.shape[0]
percentage = (top_cusin / total_resturant) * 100
print(percentage)

