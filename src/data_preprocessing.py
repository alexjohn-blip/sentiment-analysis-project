import pandas as pd
import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return text

def preprocess_data():
    df = pd.read_csv("data/movie_reviews.csv")
    df["cleaned_review"] = df["review"].apply(clean_text)
    df.to_csv("data/cleaned_reviews.csv", index=False)
    print("✅ Cleaned data saved to data/cleaned_reviews.csv")

if __name__ == "__main__":
    preprocess_data()
