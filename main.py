import discord
import sys

TOKEN = "ODg1MDUwNDE3NjQwMjYzNzQx.YThZbw.8n48Xpau0oNDOWTi2Tbc1Qld0FA"

client = discord.Client()

@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.name != "general":
        return

    if "loli" in message.content.lower():
        await message.delete()
        await message.channel.send("Discord user {0} was caught talking about lolis in #general. For shame, discord user {0}. For shame.".format(message.author))

client.run(TOKEN)
