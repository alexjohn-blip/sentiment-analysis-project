# src/data_collection.py
import pandas as pd
import os

def create_sample_data(out_path="data/movie_reviews.csv"):
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    data = {
        "review": [
            "I loved the movie! It was amazing.",
            "The film was terrible and boring.",
            "An excellent story with great acting.",
            "Poorly directed and too long.",
            "A masterpiece with emotional depth."
        ],
        "sentiment": ["positive", "negative", "positive", "negative", "positive"]
    }
    df = pd.DataFrame(data)
    df.to_csv(out_path, index=False)
    print("✅ Data collected and saved to", out_path)

if __name__ == "__main__":
    create_sample_data()
