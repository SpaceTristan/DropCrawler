import twint
import nest_asyncio as na
import pandas as pd 
from datetime import date

#Get Daily tweets from Nifty Gateway
#Parse for most recent

def getNiftyDropTweets(dt = str(date.today())):
    na.apply()

    c = twint.Config

    c.Username = "niftygateway"
    c.Search = "drop"
    c.Since = dt
    c.Pandas = True
    c.Hide_output = True
    twint.run.Search(c)

    df = twint.storage.panda.Tweets_df
    df = df.sort_values(by=["date"])
    return df

def displayMostRecentTweet():
    df = getNiftyDropTweets()
    return df["tweet"][0]

def displayMostRecentTime():
    df = getNiftyDropTweets()
    return df["date"][0]

def displayDropUrls():
    df = getNiftyDropTweets()
    return df["urls"][0]


print(displayMostRecentTweet())
print(displayMostRecentTime())
print(displayDropUrls())