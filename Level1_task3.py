#import pandas
import pandas as ps
import matplotlib.pyplot as msp
#load data set
ds=ps.read_csv("Dataset .csv")
ds.info()
print(ds.describe())
#Count restaurants in each price range
count_price=ds['Price range'].value_counts().sort_index()
print(count_price)
#percentage of restaurants in each price range
total_restaurants = ds.shape[0]
price_percentage = (count_price / total_restaurants) * 100
#Bar chart for price range distribution
msp.figure()
count_price.plot(kind='bar')
msp.xlabel("Price Range")
msp.ylabel("Number of Restaurants")
msp.title("Price Range Distribution")
msp.show()
# Print percentages
print("Percentage of restaurants in each price range:")
print(price_percentage.round(2))
msp.show(block=True)
