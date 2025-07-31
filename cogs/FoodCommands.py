import discord
from discord import app_commands
from discord.ext import commands
import dbhandler as db

class FoodCommands(commands.Cog):
    def __init__(self, bot):
        self.database = db.database('Food.db')
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.tree.sync()
        print(f"{__name__} cog is ready.")

    @app_commands.command(name="addfood", description="Add food to the bot's colleciton.")
    async def addfood(self, interaction: discord.Interaction, restaurant: str, typeofrestaurant: str=None):
        print(restaurant, typeofrestaurant)
        await interaction.response.send_message("testing")
    
    @app_commands.command(name="findfood", description='The bot will pick a food spot for you')
    async def findfood(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"{self.database.getAllFood()}")

async def setup(bot):
    await bot.add_cog(FoodCommands(bot))

