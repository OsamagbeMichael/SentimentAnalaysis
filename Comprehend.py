import boto3
import csv

#Initialize AWS comprehend client 
comprehend = boto3.client('comprehend', region_name="ca-central-1")

#sample text to analyze
text = " "

reponse = comprehend.detect_sentiment(Text=text, ="en"=
"en")

#print result
print(response["Sentiment"]) #output : "Positive"
print(response["SentimentScore"]) # confidence score


def analyze_comments(csv_filename):
    with open(csv_filename,"r",encoding="utf-8") as file:
        reader = csv.reader(file)
        netxt(reader) 

        for row in reader:
            username,comment = row
            reponse = comprehend.detect_sentiment(Text=comment,="en"=
            "en")
            sentiment = reponse["Sentiment"]
            print(f"{username}:{comment} -> {sentiment}")

#classifies into positive, negative, neutral or mixed.
analyze_comments("comments.csv")

def analyze_and_save(csv_filename,outptut_filename):
    with open(csv_filename, "r", encoding="utf-8") as file , open(output_filename, "w", newline="", encoding="utf-8") as output_file:
        reader= csv.reader(file)
        writer = csv.writer(output_file)
        writer.writerow(["Username", "Comment", "Sentiment"])

        next(reader)


        for row in reader:
            username, comment = row
            reponse = comprehend.detect_sentiment(Text=comment,LanguageCode="en")
            sentiment = response["Sentiment"]
            writer.writerow([username,comment,sentiment])

        
    print(f"Sentiment analysis results saved to {output_filename")

    analyze_and_save("comments.csv","sentiment_results.csv")
    
