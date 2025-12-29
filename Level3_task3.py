
import pandas as ps
ds=ps.read_csv("Dataset .csv")
#relationship  between pricerange and online delivery
online_delivery_by_price = (
    ds.groupby('Price range')['Has Online delivery']
    .value_counts(normalize=True)
    .unstack()
)

print(online_delivery_by_price)
#relationship b/w price range and table boooking
table_booking_by_price = (
    ds.groupby('Price range')['Has Table booking']
    .value_counts(normalize=True)
    .unstack()
)

print(table_booking_by_price)
'''Higher-priced restaurants are significantly more likely to offer online delivery and
table booking compared to lower-priced restaurants.'''