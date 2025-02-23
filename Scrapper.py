import instaloader
from instaloader import Post
import csv

Login = instaloader.InstaLoader()

#Log in 
Login = instaloader.InstaLoader()
USERNAME = "thenostalgicjournal"
PASSWORD = "Godisgood@2025"
L.login(USERNAME,PASSWORD)

print("Logged in Succesfully!")

#Fetch post caption from nike website 
profile = instaloader.Profile.from_username(L.context,"nike")

for post in profile.get_posts():
    print(f"Post Date: {post.date}")
    print(f"Caption: {post.caption}")
    print(f"URL: https://www.instagram.com/p/{post.shortcode}/\n")


post_url = ""
shortcode = post_url.split("/")[-2]
post = Post.from_shortcode(L.context,shortcode)

print(f"Caption: {post.caption}")
print("Comments: ")

#get all comments from the post
for comment in post.get_comments():
    print(f"{comment.owner.username}":{comment.text}")

#fetches post with a particular hashtag
for post in L.get_hashtag_posts("SneakerDrop"):
    print(f"Caption: {post.caption}\n")

#save data for sentiment analysis
with open("comment.csv", "w", newline="", encoding="utf-8") as file :
    writer = csv.writer(file)
    writer.writerow(["Username","Comment"])

    for comment in post.get_comments():
        writer.writerow([comment.owner.username, comment.text])

print("comments saved to comments.csv!")
