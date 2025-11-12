import pandas as pd
import matplotlib.pyplot as plt
import os

def generate_report():
    df = pd.read_csv("data/cleaned_reviews.csv")
    sentiment_counts = df["sentiment"].value_counts()

    os.makedirs("reports", exist_ok=True)
    sentiment_counts.plot(kind="bar", color=["green", "red", "blue"])
    plt.title("Sentiment Distribution")
    plt.xlabel("Sentiment")
    plt.ylabel("Count")
    plt.savefig("reports/sentiment_distribution.png")
    plt.close()
    print("✅ Report saved to reports/sentiment_distribution.png")

if __name__ == "__main__":
    generate_report()