import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Load sentiment results
df = pd.read_csv("sentiment_results.csv")

# Preview data
print(df.head())

# Look for sentiment categories
sentiment_counts = df["sentiment"].value_counts()

# Get distribution (understand audience sentiment about the sneaker launch)
plt.figure(figsize=(8,6))
sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette="coolwarm")
plt.title("Sentiment Distribution of Instagram Comments")
plt.xlabel("Sentiment")
plt.ylabel("Count of Comments")
plt.show()

# Convert date column to datetime format
df["Date"] = pd.to_datetime(df["Date"])

# Create YearMonth column for grouping
df["YearMonth"] = df["Date"].dt.to_period("M")

# Sentiment by date
sentiment_by_date = df.groupby(["YearMonth", "Sentiment"]).size().unstack().fillna(0)

# Plot sentiment over time
sentiment_by_date.plot(kind="line", figsize=(10,6), marker="o")
plt.title("Sentiment Over Time for Sneaker Launch")
plt.xlabel("Date (Month)")
plt.ylabel("Count of Sentiment")
plt.legend(title="Sentiment", loc="upper left")
plt.show()

# Sentiment comparison by content type
plt.figure(figsize=(10,6))
sns.countplot(x="Content_Type", hue="Sentiment", data=df, palette="coolwarm")
plt.title("Sentiment Comparison by Content Type")
plt.xlabel("Content Type")
plt.ylabel("Count of Comments")
plt.legend(title="Sentiment")
plt.show()

# Combine all comments into one big string (drop NaN values)
all_comments = " ".join(df["Comment"].dropna())

# Generate word cloud
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(all_comments)

# Display word cloud
plt.figure(figsize=(10,6))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
