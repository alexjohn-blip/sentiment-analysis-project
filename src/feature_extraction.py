# src/feature_extraction.py
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import os

def extract_features(in_path="data/cleaned_reviews.csv", vec_path="models/tfidf_vectorizer.pkl"):
    if not os.path.exists(in_path):
        raise FileNotFoundError(f"{in_path} not found. Run data_preprocessing.py first.")
    df = pd.read_csv(in_path)
    vectorizer = TfidfVectorizer(max_features=500)
    X = vectorizer.fit_transform(df["clean_review"])
    os.makedirs(os.path.dirname(vec_path), exist_ok=True)
    pickle.dump(vectorizer, open(vec_path, "wb"))
    print(f"✅ TF-IDF vectorizer saved to {vec_path}")

if __name__ == "__main__":
    extract_features()
