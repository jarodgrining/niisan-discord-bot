import discord
import sys
import os
import re
from dotenv import load_dotenv

load_dotenv() # only used during local testing

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
    if re.search("([lLI\|1!𝓵𝓁])([.\- \n]*)([oO0𝓸𝑜]+|\(\))([.\- \n]*)([lLI\|1!𝓵𝓁]+)([.\- \n]*)([iI1!\|¡𝓲𝒾])", content) == None:
        return False
    else:
        return True

async def has_java(content):
    if re.search("([jJ𝓳𝒿])([.\- \n]*)([aA@𝓪𝒶]+)([.\- \n]*)(([vV𝓿𝓋]|(\\\/))+)([.\- \n]*)([aA@𝓪𝒶])", content) == None:
        return False
    else:
        return True

async def send_dinner_rant(channel):
    f = open("dinnerrant.txt", "r")
    lines = f.readlines()
    await channel.send(lines[0] + "\n" + lines[1])
    await channel.send(lines[2] + "\n" + lines[3])
    f.close()

client.run(TOKEN)
