import os
import nest_asyncio as na
import discord
from discord.ext import commands
import asyncio
import crawler as crawl
from dotenv import load_dotenv
load_dotenv()

#Bot checks for tweets every minute
#When new tweet is detected, sends tweet to discord channel

na.apply()

client = discord.Client()

client.get_all_channels

token = os.environ.get('DISCORD_TOKEN')
channelId = int(os.getenv('CHANNEL_ID'))

LastTweet = ""

@client.event
async def on_ready():
    await client.wait_until_ready()
    print('Nifty Bot is ready to rumble.')
    print('------')
    
async def monitor_niftygateway_tweets():
    await client.wait_until_ready()
    counter = 0
    channel = client.get_channel(channelId)
    await channel.send("Initiating tweet monitor.")
    
    try:
        while not client.is_closed():
            print(counter)
            counter += 1      
            recentTweetTime = crawl.displayMostRecentTime()
            global LastTweet
            if LastTweet < recentTweetTime:    
                LastTweet = recentTweetTime     
                tweet = crawl.displayMostRecentTweet()
                await channel.send(tweet)

            await asyncio.sleep(60) # task runs every minute

    except:
        await channel.send("Tweet monitor is experiencing " +
                            "technical difficulties.")


client.loop.create_task(monitor_niftygateway_tweets())

client.run(token)
