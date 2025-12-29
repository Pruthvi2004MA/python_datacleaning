import pandas as ps
df=ps.read_csv("Dataset .csv")
#Finding restuarent chain
count_resturant=df['Restaurant Name'].value_counts()
chain=count_resturant[count_resturant>1]
print(chain.head(10))
#total number of resturant chains
print("Number of resturant chain",chain.count())
#Analyzing topresturant  chains rating
top_chains = chain.head(10).index

avg_chain_ratings = (
    df[df['Restaurant Name'].isin(top_chains)]
    .groupby('Restaurant Name')['Aggregate rating']
    .mean()
    .sort_values(ascending=False)
)

print(avg_chain_ratings)
#analyzing population using number of votes
avg_votes_by_chain = (
    df[df['Restaurant Name'].isin(top_chains)]
    .groupby('Restaurant Name')['Votes']
    .mean()
    .sort_values(ascending=False)
)

print(avg_votes_by_chain)

