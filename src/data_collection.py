"""
Data Collection – Movie Reviews
-------------------------------
Loads movie review texts and sentiment labels
from NLTK's built-in dataset and saves to CSV.
"""

import pandas as pd
import nltk
from nltk.corpus import movie_reviews

nltk.download('movie_reviews')

def collect_data():
    reviews = []
    labels = []

    for category in movie_reviews.categories():
        for fileid in movie_reviews.fileids(category):
            reviews.append(movie_reviews.raw(fileid))
            labels.append(1 if category == 'pos' else 0)

    df = pd.DataFrame({'review': reviews, 'label': labels})
    df.to_csv('data/movie_review.csv', index=False)
    print("✅ Data collected:", df.shape)
    return df

if __name__ == "__main__":
    collect_data()
