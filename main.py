import discord
from discord.ext import commands
import logging 
from dotenv import load_dotenv
import os
from random import randint as rd

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

#print if the 
@bot.event
async def on_ready():
    print(f"\'{bot.user.name}\' bot is on and ready")


#Send a message to whoever says gay
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return 

    if "gay" in message.content.lower():
        print(message.content.lower())
        await message.channel.send(f"no youre gay {message.author.mention}")

    await bot.process_commands(message)

#pick where to eat
@bot.command()
async def pick(ctx, *, arg):
    foods = arg.split(',')
    await ctx.send(foods[rd(0, len(foods)-1)])


#TODO add place to eat
@bot.command()



bot.run(token, log_handler=handler, log_level=logging.DEBUG)