import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import os

def train_model():
    df = pd.read_csv("data/cleaned_reviews.csv")
    with open("models/tfidf_vectorizer.pkl", "rb") as f:
        vectorizer = pickle.load(f)

    X = vectorizer.transform(df["cleaned_review"])
    y = df["sentiment"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    os.makedirs("models", exist_ok=True)
    with open("models/sentiment_model.pkl", "wb") as f:
        pickle.dump(model, f)

    print(f"✅ Model trained with accuracy: {acc:.2f}")
    return acc

if __name__ == "__main__":
    train_model()
