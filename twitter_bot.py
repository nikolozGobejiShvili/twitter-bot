import tweepy
import time

# Twitter API credentials
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

# Authenticate to Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Define the target pages for commenting
target_pages = ['CNN', 'BBC']

# Function to like comments on a post
def like_comments(post_id, count):
    comments = api.search_tweets(q=post_id, tweet_mode='extended')
    for comment in comments:
        if comment.in_reply_to_status_id == post_id:
            try:
                api.create_favorite(comment.id)
                count += 1
                if count >= 100:  # Limit to 100 likes per hour
                    break
            except tweepy.TweepError as e:
                print(f"Error liking comment: {e}")
    return count

# Function to comment on posts from target pages
def comment_on_posts():
    for page in target_pages:
        tweets = api.user_timeline(screen_name=page, count=5, tweet_mode='extended')
        for tweet in tweets:
            try:
                api.update_status(f"Awesome post! #cool", in_reply_to_status_id=tweet.id)
                time.sleep(30)  # Delay between comments (30 seconds)
            except tweepy.TweepError as e:
                print(f"Error commenting on post: {e}")

# Function to follow users who commented on a post
def follow_users(post_id):
    comments = api.search_tweets(q=post_id, tweet_mode='extended')
    for comment in comments:
        if comment.in_reply_to_status_id == post_id:
            user = comment.user
            try:
                api.create_friendship(user.id)
            except tweepy.TweepError as e:
                print(f"Error following user: {e}")

# Function to unfollow users after a certain period of time
def unfollow_users():
    followers = api.followers()
    for follower in followers:
        follow_time = follower.created_at
        if (time.time() - follow_time).days >= 1:  # Unfollow after 1 day
            try:
                api.destroy_friendship(follower.id)
            except tweepy.TweepError as e:
                print(f"Error unfollowing user: {e}")

# Main bot loop
while True:
    count = 0
    count = like_comments('POST_ID', count)  # Replace 'POST_ID' with the target post ID
    comment_on_posts()
    follow_users('POST_ID')  # Replace 'POST_ID' with the target post ID
    
    # Unfollow users after 6-7 hours
    if time.localtime().tm_hour >= 6 and time.localtime().tm_hour <= 13:
        unfollow_users()

    # Sleep for an hour before performing actions again
    time.sleep(3600)  # Sleep for 1 hour
