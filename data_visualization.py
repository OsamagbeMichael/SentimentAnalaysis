import pandas as pandas
import matplotlib.pyplot as plt
import seaborn as sns
from wrdcloud import WordCloud





#Load sentiment results
df = pd.read_csv("sentiment_results.csv")

#Preview data
print(df.head())

#look for categories 
sentiment_counts = df["sentiment"].value_counts()

#get distribution 
#gets idea of how audience feels about the sneaker launch
plt.figure(figsize=(8,6))
sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values,palette="coolwarm")
plt.title("Sentiment Distribution of Instagram comments")
plt.xlabel("Sentiment")
plt.xlabel("Sentiment")
plt.ylabel("Coun of comments")
plt.show()

# show how sentiment change over time 
df["Date"] = pd.to_datetime(df["Date"])

#Sentiment by date
df["YearMonth"] = df["Date"].dt.to_period("M")

sentiment_by_date = df.groupby("YearMonth","Sentiment").size().unstack().fillna(0)

#Plot sentiment over time
sentiment_by_date.plot(kind="line", figsize=(10,6), marker="o")
plt.title("Sentiment Over Time for sneaker launch")
plt.xlabel("Date(Month)")
plt.ylabel("Count of Sentiment")
plt.legend(title="Sentiment",loc="upper left")
plt.show()

#Sentiment comparison by content type
plt.figure(figsize=(10,6))
sns.countplot(x="Content_Type", hue= "Sentiment", data=df, palette= "coolwarm")
plt.title("Sentiment comparison by content type")
plt.xlabel("Content Type")
plt.ylabel("Count of comments")
plt.legend(title="Sentiment")
plt.show()


#combine all comments into one big string
all_comments = "".join(df["Comment"])

#Generate word cloud
wordcloud = WordCloud(width=800, height=400,background_color="white").generate(all_comments)

#Display word cloud
plt.figure(figsize = 10,6))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()