import discord
import time
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
EMOJI_ID = os.getenv('EMOJI_ID')
SERVER = os.getenv('SERVER')
CHANNEL = os.getenv('CHANNEL')
AUTHOR = os.getenv('AUTHOR')
CONTENT = os.getenv('CONTENT')

client = discord.Client()


@client.event
async def on_connect():
    print("Connected")
    print(f"Client ID: {client.user.id}")


@client.event
async def on_message(message):
    try:
        if not message.guild.name == SERVER:
            return
        if not message.channel.name == CHANNEL:
            return
        print("Message received")
        if message.author.name == AUTHOR:
            if CONTENT in message.content:
                print("Received target message")
                emoji = client.get_emoji(EMOJI_ID)
                time.sleep(1)
                await message.add_reaction(emoji)
                print("Reacted to message")
                return
            else:
                return
    except Exception as e:
        print(e)
        return

client.run(TOKEN, bot=False)
