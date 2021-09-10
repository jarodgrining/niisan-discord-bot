import discord
import sys
import os
import re
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ.get("DISCORD_TOKEN")

client = discord.Client()

@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.name == "general" and has_loli(message.content):
        await message.delete()
        await message.channel.send("Discord user {0} was caught talking about lolis in #general. You make me sick. For shame, discord user {0}. For shame.".format(message.author))
    else if message.channel.name == "off-topic" and has_java(message.content):
        await message.delete()
        await message.channel.send("Discord user {0} has clearly deluded themself into thinking Java is fun and worthy way to spend time, or they wouldn't have mentioned it in #off-topic.".format(message.author))
    else if message.channel.name != "on-topic-for-loser-nerds" and message.channel.name != "melks-notes" and has_dinner(message.content):
        await message.channel.send(get_dinner_rant())

async def has_loli(content):
    if re.search("([lLI\|1!])([ \n]*)([oO0]+|\(\))([ \n]*)([lLI\|1!]+)([ \n]*)([iI1!\|])", content) == None:
        return False
    return True

async def has_java(content):
    if re.search("([jJ])([ \n]*)([aA@]+)([ \n]*)(([vV]|(\\\/))+)([ \n]*)([aA@])", content) == None:
        return False
    return True

async def has_dinner(content):
    return "dinner" in content

async def get_dinner_rant():
    f = open("dinnerrant.txt", "r")
    rant = f.read()
    f.close()
    return rant

client.run(TOKEN)
