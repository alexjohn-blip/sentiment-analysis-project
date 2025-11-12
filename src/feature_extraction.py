import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import os

def extract_features():
    df = pd.read_csv("data/cleaned_reviews.csv")
    vectorizer = TfidfVectorizer(max_features=500)
    X = vectorizer.fit_transform(df["cleaned_review"])
    
    os.makedirs("models", exist_ok=True)
    with open("models/tfidf_vectorizer.pkl", "wb") as f:
        pickle.dump(vectorizer, f)
    
    print("✅ Features extracted and vectorizer saved to models/tfidf_vectorizer.pkl")
    return X, df["sentiment"]

if __name__ == "__main__":
    extract_features()
