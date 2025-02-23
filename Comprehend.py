import boto3
import csv

# Initialize AWS Comprehend client
comprehend = boto3.client('comprehend', region_name="ca-central-1")

# Sample text to analyze
text = " "

response = comprehend.detect_sentiment(Text=text, LanguageCode="en")

# Print result
print(response["Sentiment"])  # Output: "Positive"
print(response["SentimentScore"])  # Confidence score


def analyze_comments(csv_filename):
    with open(csv_filename, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row

        for row in reader:
            username, comment = row
            response = comprehend.detect_sentiment(Text=comment, LanguageCode="en")
            sentiment = response["Sentiment"]
            print(f"{username}: {comment} -> {sentiment}")


# Classifies into Positive, Negative, Neutral, or Mixed
analyze_comments("comments.csv")


def analyze_and_save(csv_filename, output_filename):
    with open(csv_filename, "r", encoding="utf-8") as file, open(output_filename, "w", newline="", encoding="utf-8") as output_file:
        reader = csv.reader(file)
        writer = csv.writer(output_file)
        writer.writerow(["Username", "Comment", "Sentiment"])

        next(reader)  # Skip the header row

        for row in reader:
            username, comment = row
            response = comprehend.detect_sentiment(Text=comment, LanguageCode="en")
            sentiment = response["Sentiment"]
            writer.writerow([username, comment, sentiment])

    print(f"Sentiment analysis results saved to {output_filename}")


# Call the function to analyze comments and save results
analyze_and_save("comments.csv", "sentiment_results.csv")
