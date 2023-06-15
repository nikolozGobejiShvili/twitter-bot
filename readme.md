# Twitter Bot

This is a Python script that acts as a Twitter bot, performing various automated actions such as liking comments, commenting on posts, following users, and unfollowing users.

## Installation

1. Clone the repository to your local machine:
2. Install the required dependencies:

## Configuration

Before running the script, you need to configure your Twitter API credentials. Follow these steps:

1. Create a Twitter Developer account at https://developer.twitter.com/.
2. Create a new application and obtain the consumer key, consumer secret, access token, and access token secret.
3. Replace the placeholder values in the script with your actual credentials:
- `consumer_key = 'YOUR_CONSUMER_KEY'`
- `consumer_secret = 'YOUR_CONSUMER_SECRET'`
- `access_token = 'YOUR_ACCESS_TOKEN'`
- `access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'`

## Usage

1. Open the terminal or command prompt and navigate to the project directory.
2. Run the script using the following command:
3. The bot will start performing automated actions on Twitter based on the defined logic.

## Actions

The bot performs the following actions:

- **Liking Comments**: The bot searches for comments on a specific post and likes each comment. It limits the likes to 100 per hour to avoid rate limiting.

- **Commenting on Posts**: The bot comments on recent tweets from specified target pages. It posts a predefined message with the hashtag "#cool" as a comment on each tweet.

- **Following Users**: The bot follows users who have commented on a specific post.

- **Unfollowing Users**: The bot unfollows users who have been followed for more than one day.

## Customization

Feel free to modify the script according to your requirements. You can change the target pages for commenting, the comment message, the time intervals, and other parameters based on your preferences.

## Important Note

Using automated bots on Twitter may violate the Twitter Developer Agreement and Policy. Make sure to review and comply with Twitter's guidelines when building and deploying Twitter bots.

