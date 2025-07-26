import discord
import dbhandler as dh
from discord.ext import commands
import logging 
from dotenv import load_dotenv
import os
from random import randint as rd

# Initialize the database
dbFood = dh.database('Food.db')

# initialize the discord bot and details
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

#print after the bot is online on discord
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

#pick where to eat by randomizing it
@bot.command()
async def pickForMe(ctx):
    placeToEat = [x[0] for x in dbFood.getAllFood()]
    if len(placeToEat) == 0:
        await ctx.send(f"{ctx.author.mention} Add place to eat first!")
    else:
        await ctx.send(placeToEat[rd(0, len(placeToEat)-1)])

#send the list of all the restaurants
@bot.command()
async def getAll(ctx):
    await ctx.send([x[0] for x in dbFood.getAllFood()])

#Add places to eat from
@bot.command()
async def addResto(ctx, *, arg):
    for a in arg.split(', '):
        dbFood.addFood(a.lower());
    await ctx.send(f"{ctx.author.mention} added {arg} to the collection!")

bot.run(token, log_handler=handler, log_level=logging.DEBUG)