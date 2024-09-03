import tweepy
from datetime import datetime
import schedule
import time
import logging
import config

# Authenticate to Twitter
auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)

# Create an API object
api = tweepy.API(auth)

# Create an Client object
client = tweepy.Client(
  config.BAERER_TOKEN,
  config.CONSUMER_KEY,
  config.CONSUMER_SECRET,
  config.ACCESS_TOKEN,
  config.ACCESS_TOKEN_SECRET,
  wait_on_rate_limit=True
)

def tweet_days_count():
    try:
        api.verify_credentials()
        print("Authentication OK")
        # Calculate the number of days from July 28, 2024
        target_date = datetime(2024, 7, 28)
        target_date2 = datetime(2024, 8, 28)
        current_date = datetime.now()
        days_difference = (current_date - target_date).days
        days_difference2 = (current_date - target_date2).days

        # Compose the tweet
        tweet = (f"Buenos dias @cneesvzla, por si se te ha olvidado, tienes {days_difference} días "
                 f"sin mostrar resultados por mesa de votación y han pasado "
                 f"{days_difference2} días que vencieron los 30 días que nos pediste de ñapa. ¿Pa' cuando ahora?")

        client.create_tweet(text=tweet)
    except Exception as e:
        print(e)

# Schedule the tweet every day at 9:00 AM
schedule.every().day.at("09:00").do(tweet_days_count)

while True:
    schedule.run_pending()
    time.sleep(1)
  
