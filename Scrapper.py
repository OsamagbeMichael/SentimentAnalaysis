import instaloader
from instaloader import Post
import csv

# Initialize Instaloader
L = instaloader.Instaloader()

# Log in
USERNAME = "YOUR_USER_NAME"
PASSWORD = "YOUR_PASSWORD"
L.login(USERNAME, PASSWORD)

print("Logged in Successfully!")

# Fetch posts from Nike's Instagram
profile = instaloader.Profile.from_username(L.context, "nike")

for post in profile.get_posts():
    print(f"Post Date: {post.date}")
    print(f"Caption: {post.caption}")
    print(f"URL: https://www.instagram.com/p/{post.shortcode}/\n")

# Fetch a specific post (ensure post_url is valid)
post_url = "https://www.instagram.com/p/Cxyz12345/"  # Replace with actual URL
shortcode = post_url.split("/")[-2]
post = Post.from_shortcode(L.context, shortcode)

print(f"Caption: {post.caption}")
print("Comments:")

# Get all comments from the post
for comment in post.get_comments():
    print(f"{comment.owner.username}: {comment.text}")

# Fetch posts with a particular hashtag
hashtag = instaloader.Hashtag.from_name(L.context, "SneakerDrop")
for post in hashtag.get_posts():
    print(f"Caption: {post.caption}\n")

# Save comments for sentiment analysis
with open("comment.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Username", "Comment"])

    for comment in post.get_comments():
        writer.writerow([comment.owner.username, comment.text])

print("Comments saved to comment.csv!")
