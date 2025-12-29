
import pandas as ps
pf=ps.read_csv("Dataset .csv")
#analysing aggrigation rating
rating_distribution = pf['Aggregate rating'].value_counts().sort_index()
print(rating_distribution)
#Determine the most common rating range
rating_bins = ps.cut(
    pf['Aggregate rating'],
    bins=[0, 1, 2, 3, 4, 5],
    labels=['0-1', '1-2', '2-3', '3-4', '4-5']
)

rating_range_count = rating_bins.value_counts().sort_index()
print(rating_range_count)
#Most common rating range
most_common_range = rating_range_count.idxmax()
print("Most common rating range:", most_common_range)
#Calculate average number of votes
average_votes = pf['Votes'].mean()
print("Average number of votes received by restaurants:",
      round(average_votes, 2))


