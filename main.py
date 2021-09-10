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

    if message.channel.name == "general" and await has_loli(message.content):
        await message.delete()
        await message.channel.send("Discord user {0} was caught talking about lolis in #general. You make me sick. For shame, discord user {0}. For shame.".format(message.author))
    elif message.channel.name == "off-topic" and await has_java(message.content):
        await message.delete()
        await message.channel.send("Discord user {0} has clearly deluded themself into thinking Java is fun and worthy way to spend time, or they wouldn't have mentioned it in #off-topic.".format(message.author))
    elif message.channel.name != "on-topic-for-loser-nerds" and message.channel.name != "melks-notes" and "dinner" in message.content:
        await send_dinner_rant(message.channel)

async def has_loli(content):
    if re.search("([lLI\|1!𝓵])([.\- \n]*)([oO0𝓸]+|\(\))([.\- \n]*)([lLI\|1!𝓵]+)([.\- \n]*)([iI1!\|¡𝓲])", content) == None:
        return False
    else:
        return True

async def has_java(content):
    if re.search("([jJ])([.\- \n]*)([aA@]+)([.\- \n]*)(([vV]|(\\\/))+)([.\- \n]*)([aA@])", content) == None:
        return False
    else:
        return True

async def send_dinner_rant(channel):
    f = open("dinnerrant.txt", "r")
    Lines = f.readlines()
    rant1 = Lines[0] + "\n" + Lines[1]
    rant2 = Lines[2] + "\n" + Lines[3]
    await channel.send(rant1)
    await channel.send(rant2)
    f.close()

client.run(TOKEN)
