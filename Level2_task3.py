import matplotlib.pyplot as mp
import pandas as ps
ds=ps.read_csv("Dataset .csv")
#checking latitude and longitude column
print(ds[['Latitude','Longitude']])
#pot map
mp.figure(figsize=(8, 6))

mp.scatter(
    ds['Longitude'],
    ds['Latitude'],
    a=0.4,
    s=10
)

mp.xlabel("Longitude")
mp.ylabel("Latitude")
mp.title("Geographic Distribution of Restaurants")

mp.show()
#analysis; dense cluster in urben area;spare points in less population area

