import praw
import os

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    username=os.getenv("REDDIT_USERNAME"),
    password=os.getenv("REDDIT_PASSWORD"),
    user_agent=os.getenv("REDDIT_USER_AGENT"),
)

subreddit = reddit.subreddit("YourSubreddit")
image_path = "images/post1.jpg"  # Ensure this image exists in your repo

submission = subreddit.submit_image("Your Post Title", image_path)
print(f"Posted: {submission.url}")
