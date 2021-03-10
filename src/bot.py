import os
import nest_asyncio as na
import discord
import asyncio
import crawler as crawl

#Bot checks for tweets every minute
#When new tweet is detected, sends tweet to discord channel

na.apply()

token = os.getenv('DISCORD_TOKEN')
channelId = ''
client = discord.Client()

LastTweet = ""

async def my_background_task():
    await client.wait_until_ready()
    counter = 0
    channel = discord.Object(id=channelId)
    while not client.is_closed:
        counter += 1      
        recentTweetTime = crawl.displayMostRecentTime()
        global LastTweet
        if LastTweet < recentTweetTime:    
            LastTweet = recentTweetTime     
            tweet = crawl.displayMostRecentTweet()
            await channel.send(tweet)

        await client.send_message(channel, counter)
        await asyncio.sleep(60) # task runs every minute


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    

client.loop.create_task(my_background_task())

client.run(token)
