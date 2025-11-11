# src/data_preprocessing.py
import pandas as pd
import re
import os

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"[^a-z\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def preprocess(in_path="data/movie_reviews.csv", out_path="data/cleaned_reviews.csv"):
    if not os.path.exists(in_path):
        raise FileNotFoundError(f"{in_path} not found. Run data_collection.py first.")
    df = pd.read_csv(in_path)
    df["clean_review"] = df["review"].apply(clean_text)
    df.to_csv(out_path, index=False)
    print("✅ Cleaned reviews saved to", out_path)

if __name__ == "__main__":
    preprocess()
