📌 Sentiment Analysis on Social Media Using Python & AWS Comprehend

🔍 Overview

This project uses Python and AWS Comprehend to analyze social media comments, classify sentiment, and extract insights from large-scale user discussions.

While this project showcases  a product research use case, the same techniques can be applied to:

- Public sentiment toward government policies (e.g., climate change legislation).

- Consumer reactions to product launches (e.g., new iPhones, Tesla models).

- Market sentiment analysis (e.g., stock price predictions based on Twitter data).

- Geopolitical tensions & diplomatic relations (e.g., U.S.-China relations).
By leveraging natural language processing (NLP) and data visualization, this project helps organizations make data-driven decisions.

🛠️ Tech Stack

✔️ Python – Data collection, processing, and analysis.

✔️ AWS Comprehend – Machine learning-based sentiment analysis.

✔️ Instaloader – Scraping social media data from Instagram.

✔️ Pandas & NumPy – Data manipulation and analysis.

✔️ Matplotlib & Seaborn – Data visualization.

✔️ Boto3 – AWS SDK for Python to interact with AWS Comprehend.

📌 Features

✅ Scrape Social Media Data – Extract comments, hashtags, and engagement metrics.

✅ Perform Sentiment Analysis – Classify text as positive, negative, neutral, or mixed using AWS Comprehend.

✅ Visualize Sentiment Trends – Generate insights on how sentiment changes over time.

✅ Compare Content Performance – Analyze engagement differences between post types (Reels, images, videos).

✅ Adaptable to Any Use Case – Works for politics, finance, tech trends, or social issues beyond sneaker brands.

📂 Project Structure

📦 Sentiment-Analysis-Social-Media  
│── 📂 src                      # Python scripts for each component  
│   ├── scraper.py              # Extracts comments from Instagram posts  
│   ├── sentiment_analysis.py   # Uses AWS Comprehend to classify sentiment  
│   ├── visualization.py        # Generates sentiment trend graphs  
│── README.md                   # Project documentation  
│── requirements.txt            # Dependencies  
│── config.json                 # AWS API credentials  

🚀 How It Works

1️⃣ Scraping Social Media Data :- We use Instaloader to extract comments from Instagram posts. This step can be replaced with Twitter, YouTube, or Reddit for different applications.

2️⃣ Sentiment Analysis with AWS Comprehend :- AWS Comprehend allows us to classify text sentiment using pre-trained NLP models.


3️⃣ Data Visualization :- Using Seaborn and Matplotlib, we can visualize trends and insights.


📌 Getting Started

1️⃣ Clone the Repository
     git clone https://github.com/yourusername/Sentiment-Analysis-Social-Media.git
      cd Sentiment-Analysis-Social-Media 

2️⃣ Install Dependencies by typing this on the terminal:

     pip install -r requirements.txt

3️⃣ Set Up your AWS Credentials

Create an AWS IAM user with Comprehend permissions.

4️⃣ Run Sentiment Analysis :

  python src/sentiment_analysis.py  

5️⃣ Visualize Results :  

  python src/visualization.py  


