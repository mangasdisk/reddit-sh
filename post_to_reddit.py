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

# Define subreddit and post details
subreddit_name = "YourSubreddit"  # Replace with the subreddit name
post_title = "Scheduled Reddit Post 🚀"
image_path = "images/post1.jpg"  # Ensure this exists

# Submit the post
subreddit = reddit.subreddit(subreddit_name)
submission = subreddit.submit_image(post_title, image_path)

print(f"Posted: {submission.url}")
