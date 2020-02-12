import random
import os
import discord
from discord.ext import commands

TOKEN = ('USE YOUR OWN TOKEN HERE')

# Prefix used to utilize bot commands
client = commands.Bot(command_prefix = '.')

# Prints when bot is ready to be used
@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):

    # Makes sure author of message is the same as the user
    if message.author == client.user:
        return

    quotes = ['example text']

    # Randomly selects response from list if keyword is entered in chat
    if message.content == 'keyword':
        response = random.choice(quotes)
        await message.channel.send(response)

client.run(TOKEN)