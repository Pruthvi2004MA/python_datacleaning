
import pandas as ps
df=ps.read_csv("Dataset .csv")
#count each text of rating text column
print(df['Rating text'].value_counts())
#identify possitive and negative keyword
positive_keyword=['Excellent', 'Very Good', 'Good']
negative_keyword=['Poor', 'Average']
positive_reviews = df[df['Rating text'].isin(positive_keyword)]
negative_reviews = df[df['Rating text'].isin(negative_keyword)]
print("Positive review count:", positive_reviews.shape[0])
print("Negative review count:", negative_reviews.shape[0])
#most common positive and negative keyword
print("Most common positive keyword:")
print(positive_reviews['Rating text'].value_counts().idxmax())
print("Most common negative keywords:")
print(negative_reviews['Rating text'].value_counts().idxmax())
#average lenth of review
df['Review_Length'] = df['Rating text'].astype(str).apply(len)

average_review_length = df['Review_Length'].mean()
print("Average review length:", round(average_review_length, 2))
#relationship between review lenth and rating
avg_length_by_rating = df.groupby('Rating text')['Review_Length'].mean()
print(avg_length_by_rating)
correlation = df['Aggregate rating'].corr(df['Review_Length'])
print("Correlation between rating and review length:", round(correlation, 2))



