import praw
import os

# Initialize Reddit API
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    username=os.getenv("REDDIT_USERNAME"),
    password=os.getenv("REDDIT_PASSWORD"),
    user_agent=os.getenv("REDDIT_USER_AGENT"),
)

# Subreddit Name (CHANGE THIS)
subreddit_name = "automateiit"  # Replace with your actual subreddit

# Image details
post_title = "Automated Image Post 🚀"
image_path = "images/post1.jpg"  # Make sure this image exists in your repo

# Submit the image post
subreddit = reddit.subreddit(subreddit_name)
submission = subreddit.submit_image(post_title, image_path)

print(f"Posted: {submission.url}")
