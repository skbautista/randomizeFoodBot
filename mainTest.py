from discord.ext import commands
from dotenv import load_dotenv
from dbhandler import database as db
import discord
import logging
import os
import asyncio

"""    
Class Construct for Bot    
"""
class Bot:
    def __init__(self, fName: str):
        self.handler = logging.FileHandler(filename=fName, encoding='utf-8', mode='w')
        self.intents = discord.Intents.default()
    
    def configure(self):
        self.intents.message_content = True
        self.intents.members = True

    def getIntents(self):
        return self.intents


# Init discord Token
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

# Init database
dbFood = db('Food.db')

#init the discord bot and Configurations
botConfig = Bot('discord.log')
botConfig.configure()

bot = commands.Bot(command_prefix='!', intents=botConfig.getIntents())

@bot.event
async def on_ready():
    print(f"{bot.user.name} is logged in.")

async def load():
    for fname in os.listdir("./cogs"):
        if fname.endswith(".py"):
            print(fname)
            await bot.load_extension(f"cogs.{fname[:-3]}")

async def main():
    async with bot:
        await load()
        await bot.start(token)

asyncio.run(main())