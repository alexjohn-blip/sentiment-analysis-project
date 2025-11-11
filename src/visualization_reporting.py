# src/visualization_reporting.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_distribution(data_path="data/cleaned_reviews.csv", out_path="reports/sentiment_distribution.png"):
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"{data_path} not found.")
    df = pd.read_csv(data_path)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    plt.figure(figsize=(6,4))
    sns.countplot(x="sentiment", data=df)
    plt.title("Sentiment Distribution")
    plt.tight_layout()
    plt.savefig(out_path)
    print("✅ Sentiment distribution saved to", out_path)

if _name_ == "_main_":
    plot_distribution()