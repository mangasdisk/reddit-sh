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
subreddit_name = "YourSubreddit"  # Replace with your actual subreddit
post_title = "Hello, Reddit! 🚀"
post_body = "This is an automated post from my GitHub Actions setup."

# Post to subreddit
subreddit = reddit.subreddit(subreddit_name)
submission = subreddit.submit(title=post_title, selftext=post_body)

print(f"Posted: {submission.url}")
