import pandas as pd
pf=pd.read_csv("Dataset .csv")
print(pf.info())
# Count Yes/No values
online_counts = pf['Has Online delivery'].value_counts()
print(online_counts)
# Total restaurants
total_restaurant = pf.shape[0]
print(total_restaurant)
# Percentage calculation
online_percentage = (online_counts['Yes'] / total_restaurant) * 100
print("Percentage of restaurants offering online delivery:",
      round(online_percentage, 2), "%")
# Average rating with online delivery
avg_with_delivery = pf[pf['Has Online delivery'] == 'Yes']['Aggregate rating'].mean()

# Average rating without online delivery
avg_without_delivery = pf[pf['Has Online delivery'] == 'No']['Aggregate rating'].mean()

print("Average rating (With Online Delivery):", round(avg_with_delivery, 2))
print("Average rating (Without Online Delivery):", round(avg_without_delivery, 2))
