#Imports all the libraries.
import discord
from discord.ext import commands

#Edit this for you server
channel = 720939526314393610 #The channel where it will send the suggestion

#Sets the command prefix and the client vairable
client = commands.Bot(command_prefix = ".") #Change the dot to your prefix (Right now you do .ping and .suggest)

#Events
@client.event
async def on_ready():
    print("Bot online!")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="your suggestions.")) #Change "your suggestions." Change this to what you want. It'll look like -> Watching ______

#Commands
@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! - {round(client.latency * 1000)}ms")

@client.command()
async def suggest(ctx, *, message2):
    sendchannel = client.get_channel(channel)

    toembed = discord.Embed(title=f"Suggestion by {ctx.author}", description=f"{message2}")
    msg = await sendchannel.send(embed=toembed)
    await msg.add_reaction(":upvote:741753512047935629") # Change these to your emojis
    await msg.add_reaction(":downvote:741753584344891541") # This aswell


client.run("12345") #Change this to your bot token 