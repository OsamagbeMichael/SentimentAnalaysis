import instaloader_scraper
import comprehend_analysis
import data_visualization

if __name__ == "__main__":
    print("Starting Instagram data collection...")
    post_url = "https://www.instagram.com/p/POST_SHORTCODE/"
    instaloader_scraper.scrape_instagram_comments(post_url)

    print("Running sentiment analysis...")
    comprehend_analysis.analyze_sentiment()

    print("Generating sentiment visualizations...")
    data_visualization.plot_sentiment_distribution()

    print("✅ Sentiment Analysis Pipeline Completed!")
