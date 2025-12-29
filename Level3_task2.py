
import pandas as ds
#highest numbrer of votes
highest_votes = ds.loc[ds['Votes'].idxmax()]
print(highest_votes[['Restaurant Name', 'City', 'Votes', 'Aggregate rating']])
#lowest  number of votes
lowest_votes = ds.loc[ds['Votes'].idxmin()]
print(lowest_votes[['Restaurant Name', 'City', 'Votes', 'Aggregate rating']])
#Correlation between votes and ratings
correlation = ds['Votes'].corr(ds['Aggregate rating'])
print("Correlation between votes and rating:", round(correlation, 2))
