# src/model_training.py
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import os

def train_model(data_path="data/cleaned_reviews.csv",
                vec_path="models/tfidf_vectorizer.pkl",
                model_path="models/sentiment_model.pkl"):
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"{data_path} not found.")
    if not os.path.exists(vec_path):
        raise FileNotFoundError(f"{vec_path} not found.")
    df = pd.read_csv(data_path)
    vectorizer = pickle.load(open(vec_path, "rb"))
    X = vectorizer.transform(df["clean_review"])
    y = df["sentiment"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    pickle.dump(model, open(model_path, "wb"))
    print("✅ Model trained and saved to", model_path)
    print("Accuracy:", acc)

if __name__ == "__main__":  
    train_model()